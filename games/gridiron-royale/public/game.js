import * as THREE from "three";
import { GLTFLoader } from "./vendor/GLTFLoader.js";
import { clone as skeletonClone } from "./vendor/SkeletonUtils.js";
import { STR } from "./strings.js";

const bootMark = (s) => { document.documentElement.dataset.boot = s; };
bootMark("module-start");

/* ============================== CONFIG (balance data, see design/thresholds.md + design/OS_PULL_V2.md) */
const CFG = {
  fieldW: 40, driveLen: 80, endzoneLen: 10,
  baseSpeed: 10, sprintSpeed: 15, backPedal: 0.55,
  staminaMax: 100, staminaDrain: 30, staminaRegen: 18, staminaGate: 15,
  jukeDash: 24, jukeTime: 0.25, jukeInvuln: 0.4, jukeCd: 1.2,
  spinTime: 0.5, spinRadius: 2.0, spinCd: 3.0,
  tackleRadius: 1.3, defKnockTime: 1.6, defRecycleBehind: 6,
  defBaseCount: 4, defMaxCount: 10, defBaseSpeed: 8, defSpeedPerWave: 0.8, defSpeedMax: 12.5,
  matchTime: 120, downsMax: 4, tdPoints: 7, goldPoints: 3, mvpScore: 21,
  clutchPerDown: 0.04, burstMult: 1.25, burstTime: 1.5,
  orbStamina: 40, orbCount: 3, goldChance: 0.35, boostPads: 2,
  dropHeight: 36, dropFall: 11,
  chainWindow: 10, chainNearDist: 4.5, chainBonus: [0, 0, 3, 7],
  heroHeight: 2.0, defHeight: 2.0, tankScale: 1.16, blitzScale: 0.94,
  confettiMax: 600, crowdCount: 1200, dprCap: 1.5,
};

/* ============================== seeded RNG */
function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/* ============================== INPUT · everything becomes one command object */
const BIND = {
  KeyW: "up", KeyS: "down", KeyA: "left", KeyD: "right",
  ArrowUp: "up", ArrowDown: "down", ArrowLeft: "left", ArrowRight: "right",
  ShiftLeft: "sprint", ShiftRight: "sprint",
  KeyQ: "jukeL", KeyE: "jukeR", Space: "spin",
};
const PAD = { 0: "sprint", 1: "spin", 4: "jukeL", 5: "jukeR" };
const held = new Set();
let anyKeyPulse = false;
let padsConnected = false, padAnyPrev = false;
addEventListener("gamepadconnected", () => { padsConnected = true; });
addEventListener("gamepaddisconnected", () => { padsConnected = !!(navigator.getGamepads && [...navigator.getGamepads()].some(Boolean)); });
addEventListener("keydown", (e) => {
  if (!e.repeat) anyKeyPulse = true;
  const c = BIND[e.code];
  if (c) { held.add(c); e.preventDefault(); }
});
addEventListener("keyup", (e) => { const c = BIND[e.code]; if (c) held.delete(c); });

const touchState = { stickId: -1, ox: 0, oy: 0, x: 0, y: 0, sprint: false, jukeL: false, jukeR: false, spin: false };
addEventListener("pointerdown", (e) => {
  anyKeyPulse = true;
  if (e.pointerType === "touch") {
    showTouchButtons();
    if (e.clientX < innerWidth * 0.5 && touchState.stickId === -1) {
      touchState.stickId = e.pointerId; touchState.ox = e.clientX; touchState.oy = e.clientY;
      touchState.x = 0; touchState.y = 0;
    }
  }
});
addEventListener("pointermove", (e) => {
  if (e.pointerId === touchState.stickId) {
    const dx = e.clientX - touchState.ox, dy = e.clientY - touchState.oy, r = 50;
    touchState.x = Math.max(-1, Math.min(1, dx / r));
    touchState.y = Math.max(-1, Math.min(1, dy / r));
  }
});
function endTouch(e) {
  if (e.pointerId === touchState.stickId) { touchState.stickId = -1; touchState.x = 0; touchState.y = 0; }
}
addEventListener("pointerup", endTouch);
addEventListener("pointercancel", endTouch);

function bindBtn(id, prop) {
  const el = document.getElementById(id);
  el.addEventListener("pointerdown", (e) => { touchState[prop] = true; anyKeyPulse = true; e.stopPropagation(); e.preventDefault(); });
  el.addEventListener("pointerup", () => { touchState[prop] = false; });
  el.addEventListener("pointercancel", () => { touchState[prop] = false; });
}
bindBtn("btnSprint", "sprint"); bindBtn("btnJukeL", "jukeL"); bindBtn("btnJukeR", "jukeR"); bindBtn("btnSpin", "spin");
function showTouchButtons() {
  for (const id of ["btnSprint", "btnJukeL", "btnJukeR", "btnSpin"]) document.getElementById(id).style.display = "flex";
}

const cmd = { x: 0, z: 0, sprint: false, jukeL: false, jukeR: false, spin: false, any: false };
function readCommands() {
  let x = 0, z = 0;
  if (held.has("left")) x -= 1;
  if (held.has("right")) x += 1;
  if (held.has("up")) z += 1;
  if (held.has("down")) z -= 1;
  let sprint = held.has("sprint"), jukeL = held.has("jukeL"), jukeR = held.has("jukeR"), spin = held.has("spin");
  x += touchState.x; z += -touchState.y;
  sprint = sprint || touchState.sprint; jukeL = jukeL || touchState.jukeL; jukeR = jukeR || touchState.jukeR; spin = spin || touchState.spin;
  const pads = padsConnected && navigator.getGamepads ? navigator.getGamepads() : null;
  let padAny = false;
  if (pads) for (let i = 0; i < pads.length; i++) {
    const gp = pads[i]; if (!gp) continue;
    if (Math.abs(gp.axes[0]) > 0.18) x += gp.axes[0];
    if (Math.abs(gp.axes[1]) > 0.18) z += -gp.axes[1];
    for (let b = 0; b < gp.buttons.length; b++) {
      if (!gp.buttons[b].pressed) continue;
      padAny = true;
      const c = PAD[b];
      if (c === "sprint") sprint = true; else if (c === "spin") spin = true;
      else if (c === "jukeL") jukeL = true; else if (c === "jukeR") jukeR = true;
    }
  }
  cmd.x = Math.max(-1, Math.min(1, x));
  cmd.z = Math.max(-1, Math.min(1, z));
  cmd.sprint = sprint; cmd.jukeL = jukeL; cmd.jukeR = jukeR; cmd.spin = spin;
  if (padAny && !padAnyPrev) anyKeyPulse = true; // rising edge only
  padAnyPrev = padAny;
  cmd.any = anyKeyPulse; anyKeyPulse = false;
  return cmd;
}

/* ============================== AUDIO · WebAudio, gain staging, ducking, safety limiter */
const AUDIO_FILES = {
  music: "./assets/music.m4a",
  ambience: "./assets/sfx_crowd_loop.mp3",
  whistle: "./assets/sfx_whistle.mp3",
  tackle: "./assets/sfx_tackle.mp3",
  juke: "./assets/sfx_juke.mp3",
  touchdown: "./assets/sfx_touchdown.mp3",
  pickup: "./assets/sfx_pickup.mp3",
  voWelcome: "./assets/vo_welcome.wav",
  voTouchdown: "./assets/vo_touchdown.wav",
  voMvp: "./assets/vo_mvp.wav",
  voLastdown: "./assets/vo_lastdown.wav",
  voHothand: "./assets/vo_hothand.wav",
  voTurnover: "./assets/vo_turnover.wav",
  voGoldenball: "./assets/vo_goldenball.wav",
};
const GAINS = {
  music: 0.3, whistle: 0.7, tackle: 0.8, juke: 0.5, touchdown: 0.9, pickup: 0.6,
  voWelcome: 1.0, voTouchdown: 1.0, voMvp: 1.0, voLastdown: 1.0,
  voHothand: 1.0, voTurnover: 1.0, voGoldenball: 0.9, ambient: 0.12, ambience: 0.12,
};
const audio = { ctx: null, buffers: {}, master: null, musicGain: null, musicSrc: null, ambientSrc: null, duckUntil: 0 };
function audioInit() {
  if (audio.ctx) { if (audio.ctx.state === "suspended") audio.ctx.resume(); return; }
  const Ctx = window.AudioContext || window.webkitAudioContext;
  if (!Ctx) return;
  audio.ctx = new Ctx();
  const comp = audio.ctx.createDynamicsCompressor();
  comp.threshold.value = -8; comp.ratio.value = 12;
  const master = audio.ctx.createGain(); master.gain.value = 0.85;
  master.connect(comp); comp.connect(audio.ctx.destination);
  audio.master = master;
  for (const name of Object.keys(AUDIO_FILES)) {
    fetch(AUDIO_FILES[name])
      .then((r) => (r.ok ? r.arrayBuffer() : Promise.reject(new Error("missing " + name))))
      .then((ab) => audio.ctx.decodeAudioData(ab))
      .then((buf) => {
        audio.buffers[name] = buf;
        if (name === "music" && state.mode !== "title") startMusic();
        if ((name === "ambience" || name === "touchdown") && state.mode !== "title") startAmbient();
      })
      .catch(() => {});
  }
}
function playSfx(name, gain) {
  if (!audio.ctx || !audio.buffers[name]) return 0;
  const src = audio.ctx.createBufferSource();
  src.buffer = audio.buffers[name];
  const g = audio.ctx.createGain(); g.gain.value = gain != null ? gain : (GAINS[name] || 0.7);
  src.connect(g); g.connect(audio.master); src.start();
  return src.buffer.duration;
}
function playVo(name) {
  const dur = playSfx(name);
  if (dur > 0 && audio.musicGain) {
    const t = audio.ctx.currentTime;
    audio.musicGain.gain.cancelScheduledValues(t);
    audio.musicGain.gain.setValueAtTime(0.1, t);
    audio.musicGain.gain.linearRampToValueAtTime(GAINS.music, t + dur + 0.4);
  }
}
function startMusic() {
  if (!audio.ctx || !audio.buffers.music || audio.musicSrc) return;
  const src = audio.ctx.createBufferSource();
  src.buffer = audio.buffers.music; src.loop = true;
  const g = audio.ctx.createGain(); g.gain.value = GAINS.music;
  src.connect(g); g.connect(audio.master); src.start();
  audio.musicSrc = src; audio.musicGain = g;
}
function startAmbient() {
  const bed = audio.buffers.ambience || audio.buffers.touchdown;
  if (!audio.ctx || !bed || audio.ambientSrc) return;
  const src = audio.ctx.createBufferSource();
  src.buffer = bed; src.loop = true;
  const g = audio.ctx.createGain(); g.gain.value = GAINS.ambient;
  src.connect(g); g.connect(audio.master); src.start();
  audio.ambientSrc = src; audio.ambientGain = g;
}
// withhold-then-reveal (OS_PULL_V2 P13): crowd drops as the MVP run builds, releases at 21
function setAmbientLevel(mult) {
  if (audio.ambientGain && audio.ctx) {
    audio.ambientGain.gain.linearRampToValueAtTime(GAINS.ambient * mult, audio.ctx.currentTime + 0.8);
  }
}

/* ============================== RENDERER / SCENE */
const canvas = document.getElementById("c");
let renderer;
try {
  renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
} catch (err) {
  document.getElementById("titleH").textContent = STR.title;
  document.getElementById("tagline").textContent = STR.webglRequired;
  document.title = STR.title;
  throw err;
}
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping; // one grade for everything (OS_PULL_V2 P6)
bootMark("renderer-ok");
const scene = new THREE.Scene();
scene.fog = new THREE.Fog(0xc97bd9, 90, 260);
const camera = new THREE.PerspectiveCamera(58, 1, 0.1, 600);
function resize() {
  const dpr = Math.min(devicePixelRatio || 1, CFG.dprCap);
  renderer.setPixelRatio(dpr);
  renderer.setSize(innerWidth, innerHeight);
  camera.aspect = innerWidth / innerHeight;
  camera.updateProjectionMatrix();
}
addEventListener("resize", resize);
addEventListener("orientationchange", resize);
resize();

const hemi = new THREE.HemisphereLight(0xbfe8ff, 0x3c2a6e, 0.9);
scene.add(hemi);
const sun = new THREE.DirectionalLight(0xffe2b0, 1.5);
sun.position.set(-40, 60, 20);
scene.add(sun);

/* ============================== WORLD · field, sky panorama, islands, stands, crowd, towers */
const fieldLen = CFG.driveLen + 2 * CFG.endzoneLen;

// Asset: turf_field (procedural per FORMULA; endzone wordmarks from STR)
function makeFieldTexture() {
  const c = document.createElement("canvas");
  c.width = 1024; c.height = 2048;
  const g = c.getContext("2d");
  const zoneH = (CFG.endzoneLen / fieldLen) * c.height;
  const playH = c.height - 2 * zoneH;
  const stripes = 16;
  for (let i = 0; i < stripes; i++) {
    g.fillStyle = i % 2 ? "#1fae62" : "#23c06d";
    g.fillRect(0, zoneH + (playH * i) / stripes, c.width, playH / stripes + 1);
  }
  g.fillStyle = "#5a2d9e"; g.fillRect(0, 0, c.width, zoneH);
  g.fillStyle = "#6c37bd"; g.fillRect(0, c.height - zoneH, c.width, zoneH);
  g.fillStyle = "#ffd34d";
  g.fillRect(0, zoneH - 10, c.width, 10);
  g.fillRect(0, c.height - zoneH, c.width, 10);
  g.font = "900 120px Arial Black, Arial";
  g.textAlign = "center"; g.textBaseline = "middle";
  g.fillStyle = "rgba(255,211,77,0.92)";
  g.save(); g.translate(c.width / 2, c.height - zoneH / 2); g.scale(1, -1); g.fillText(STR.endzoneA, 0, 0); g.restore();
  g.save(); g.translate(c.width / 2, zoneH / 2); g.scale(1, -1); g.fillText(STR.endzoneB, 0, 0); g.restore();
  g.fillStyle = "rgba(255,255,255,0.85)";
  for (let i = 1; i < 8; i++) g.fillRect(0, zoneH + (playH * i) / 8 - 3, c.width, 6);
  for (let i = 0; i < 40; i++) {
    const y = zoneH + (playH * i) / 40;
    g.fillRect(c.width * 0.31, y - 2, 26, 4);
    g.fillRect(c.width * 0.69 - 26, y - 2, 26, 4);
  }
  g.fillRect(0, 0, 14, c.height); g.fillRect(c.width - 14, 0, 14, c.height);
  const tex = new THREE.CanvasTexture(c);
  tex.colorSpace = THREE.SRGBColorSpace;
  tex.anisotropy = 4;
  return tex;
}
const field = new THREE.Mesh(
  new THREE.PlaneGeometry(CFG.fieldW + 4, fieldLen),
  new THREE.MeshLambertMaterial({ map: makeFieldTexture() })
);
field.rotation.x = -Math.PI / 2;
field.rotation.z = Math.PI; // texture v=0 at far end; flip so endzoneA reads at the goal line ahead
field.position.set(0, 0, CFG.driveLen / 2);
scene.add(field);

const islandBase = new THREE.Mesh(
  new THREE.CylinderGeometry(0.1, 34, 26, 9, 1),
  new THREE.MeshLambertMaterial({ color: 0x6b4a86 })
);
islandBase.scale.set(1.4, 1, 2.2);
islandBase.position.set(0, -13.2, CFG.driveLen / 2);
scene.add(islandBase);

// Asset: sky_pano (generated panorama on a mirrored-wrap cylinder; seam hidden by mirroring)
const skyTexLoader = new THREE.TextureLoader();
const panoTex = skyTexLoader.load("./assets/sky_pano.jpg");
panoTex.colorSpace = THREE.SRGBColorSpace;
panoTex.wrapS = THREE.MirroredRepeatWrapping;
panoTex.repeat.x = 2;
const panoMat = new THREE.MeshBasicMaterial({ map: panoTex, side: THREE.BackSide, fog: false });
const panoCyl = new THREE.Mesh(new THREE.CylinderGeometry(260, 260, 150, 32, 1, true), panoMat);
panoCyl.position.set(0, 38, CFG.driveLen / 2);
scene.add(panoCyl);

// gradient cap dome above/below the panorama
function makeSkyTexture() {
  const c = document.createElement("canvas");
  c.width = 4; c.height = 512;
  const g = c.getContext("2d");
  const grad = g.createLinearGradient(0, 0, 0, 512);
  grad.addColorStop(0, "#3fa9f5");
  grad.addColorStop(0.55, "#7fc4f8");
  grad.addColorStop(0.78, "#e58dde");
  grad.addColorStop(1, "#f7b267");
  g.fillStyle = grad; g.fillRect(0, 0, 4, 512);
  const tex = new THREE.CanvasTexture(c);
  tex.colorSpace = THREE.SRGBColorSpace;
  return tex;
}
const skyMat = new THREE.MeshBasicMaterial({ map: makeSkyTexture(), side: THREE.BackSide, fog: false });
const sky = new THREE.Mesh(new THREE.SphereGeometry(330, 24, 14), skyMat);
sky.position.set(0, 0, CFG.driveLen / 2);
scene.add(sky);

const islands = [];
{
  const rockMat = new THREE.MeshLambertMaterial({ color: 0x7a5a9e });
  const grassMat = new THREE.MeshLambertMaterial({ color: 0x2ecf77 });
  const spots = [[-90, 18, 30], [95, 30, 70], [-80, 44, 120], [88, 12, -20], [-100, 26, 160]];
  for (const [x, y, z] of spots) {
    const grp = new THREE.Group();
    const rock = new THREE.Mesh(new THREE.ConeGeometry(12, 16, 7), rockMat);
    rock.rotation.x = Math.PI;
    const top = new THREE.Mesh(new THREE.CylinderGeometry(12, 12.5, 3, 7), grassMat);
    top.position.y = 9.5;
    grp.add(rock, top);
    grp.position.set(x, y, z);
    grp.userData.baseY = y;
    grp.userData.phase = x * 0.13;
    scene.add(grp);
    islands.push(grp);
  }
}

{
  const standMat = new THREE.MeshLambertMaterial({ color: 0x4a2f8f });
  for (const sideX of [-1, 1]) {
    const stand = new THREE.Mesh(new THREE.BoxGeometry(10, 9, fieldLen + 8), standMat);
    stand.position.set(sideX * (CFG.fieldW / 2 + 8), 3.4, CFG.driveLen / 2);
    stand.rotation.z = sideX * -0.18;
    scene.add(stand);
  }
}
const crowd = (() => {
  const crowdGeo = new THREE.BoxGeometry(0.7, 0.9, 0.7);
  const crowdMat = new THREE.MeshLambertMaterial();
  const mesh = new THREE.InstancedMesh(crowdGeo, crowdMat, CFG.crowdCount);
  const dummy = new THREE.Object3D();
  const col = new THREE.Color();
  const crng = mulberry32(1234567);
  for (let i = 0; i < CFG.crowdCount; i++) {
    const side = i % 2 ? 1 : -1;
    const row = Math.floor(crng() * 6);
    dummy.position.set(
      side * (CFG.fieldW / 2 + 4.6 + row * 1.55),
      3.2 + row * 1.25,
      -8 + crng() * (fieldLen + 4)
    );
    dummy.rotation.y = side > 0 ? -Math.PI / 2 : Math.PI / 2;
    dummy.updateMatrix();
    mesh.setMatrixAt(i, dummy.matrix);
    col.setHSL(crng(), 0.75, 0.45 + crng() * 0.25);
    mesh.setColorAt(i, col);
  }
  mesh.instanceMatrix.needsUpdate = true;
  if (mesh.instanceColor) mesh.instanceColor.needsUpdate = true;
  scene.add(mesh);
  return mesh;
})();

// stadium light towers: emissive heads switch on as the night games start
const towers = [];
{
  const poleMat = new THREE.MeshLambertMaterial({ color: 0x2d1a5e });
  for (const [sx, sz] of [[-1, -6], [1, -6], [-1, CFG.driveLen + 6], [1, CFG.driveLen + 6]]) {
    const grp = new THREE.Group();
    const pole = new THREE.Mesh(new THREE.CylinderGeometry(0.5, 0.7, 22, 6), poleMat);
    pole.position.y = 11;
    const headMat = new THREE.MeshLambertMaterial({ color: 0xfff6d8, emissive: 0xfff6d8, emissiveIntensity: 0 });
    const head = new THREE.Mesh(new THREE.BoxGeometry(5, 2, 1), headMat);
    head.position.y = 22.6;
    head.lookAt(0, 0, CFG.driveLen / 2);
    grp.add(pole, head);
    grp.position.set(sx * (CFG.fieldW / 2 + 13), 0, sz);
    scene.add(grp);
    towers.push(headMat);
  }
}

/* ============================== CHARACTERS · rigged GLBs (image-to-3D, run clips baked) */
const ASSETS = {
  heroRun: "./assets/hero_run.glb",
  heroDance: "./assets/hero_dance.glb", // optional; fallback handled
  defenderRun: "./assets/defender_run.glb",
};
const shadowMat = new THREE.MeshBasicMaterial({ color: 0x10052e, transparent: true, opacity: 0.32 });
const shadowGeo = new THREE.CircleGeometry(0.8, 14);

const loaderGLTF = new GLTFLoader();
function loadGLB(url) {
  return new Promise((res, rej) => loaderGLTF.load(url, res, undefined, rej));
}
const _box = new THREE.Box3();
const _size = new THREE.Vector3();
function normalizeToHeight(obj, targetH) {
  _box.setFromObject(obj);
  _box.getSize(_size);
  const s = targetH / (_size.y || 1);
  obj.scale.setScalar(s);
  _box.setFromObject(obj);
  obj.position.y -= _box.min.y;
  return s;
}
function stripRootDrift(animations) {
  // image-to-3D library clips can bake forward root motion into Hips.position;
  // pin X/Z to frame zero so the character runs in place (Y bob preserved)
  for (const clip of animations) {
    for (const t of clip.tracks) {
      if (t.name.endsWith(".position") && /hips|root|pelvis|armature/i.test(t.name)) {
        const v = t.values;
        for (let i = 3; i < v.length; i += 3) { v[i] = v[0]; v[i + 2] = v[2]; }
      }
    }
  }
}
function makeRig(gltfScene, animations, targetH) {
  const root = new THREE.Group();
  const model = gltfScene;
  stripRootDrift(animations);
  normalizeToHeight(model, targetH);
  root.add(model);
  const shadow = new THREE.Mesh(shadowGeo, shadowMat);
  shadow.rotation.x = -Math.PI / 2; shadow.position.y = 0.02;
  root.add(shadow);
  const mixer = new THREE.AnimationMixer(model);
  const runAction = animations.length ? mixer.clipAction(animations[0]) : null;
  if (runAction) runAction.play();
  return { root, model, mixer, runAction };
}

let hero = null;            // rig
let heroDance = null;       // {root, mixer} separate model swapped in for the TD emote
let danceAvailable = false;
const defenders = [];       // {rig, active, type, downTimer, staggerTimer, speed, pos, baseScale, radius}
let ballMesh = null, ballBone = null;
const canopy = new THREE.Group();
{
  const top = new THREE.Mesh(new THREE.BoxGeometry(2.6, 0.18, 1.2), new THREE.MeshLambertMaterial({ color: 0x27e0ff }));
  top.position.y = 3.4;
  const strapM = new THREE.MeshLambertMaterial({ color: 0xfff2dd });
  const s1 = new THREE.Mesh(new THREE.BoxGeometry(0.05, 1.6, 0.05), strapM);
  s1.position.set(-1.0, 2.6, 0); s1.rotation.z = 0.42;
  const s2 = new THREE.Mesh(new THREE.BoxGeometry(0.05, 1.6, 0.05), strapM);
  s2.position.set(1.0, 2.6, 0); s2.rotation.z = -0.42;
  canopy.add(top, s1, s2);
}

const DEF_TYPES = {
  chaser: { tint: 0xffffff, scale: 1.0, speedMult: 1.0, radius: CFG.tackleRadius, anim: 1.0 },
  blitzer: { tint: 0xff9be8, scale: CFG.blitzScale, speedMult: 1.25, radius: CFG.tackleRadius, anim: 1.3 },
  tank: { tint: 0x8f7ae0, scale: CFG.tankScale, speedMult: 0.75, radius: 2.0, anim: 0.85 },
};

async function bootAssets() {
  const [heroG, defG] = await Promise.all([loadGLB(ASSETS.heroRun), loadGLB(ASSETS.defenderRun)]);
  hero = makeRig(heroG.scene, heroG.animations, CFG.heroHeight);
  scene.add(hero.root);
  hero.root.add(canopy);
  // football prop follows the hand bone when one exists
  ballMesh = new THREE.Mesh(new THREE.SphereGeometry(0.2, 8, 6), new THREE.MeshLambertMaterial({ color: 0x8a4b1f }));
  ballMesh.scale.set(1.3, 0.8, 0.8);
  scene.add(ballMesh);
  hero.model.traverse((o) => {
    if (!ballBone && o.isBone && /hand|wrist/i.test(o.name) && /r($|[^a-z])|right/i.test(o.name)) ballBone = o;
  });
  // defender pool: cloned skinned meshes, per-type tinted materials
  for (let i = 0; i < CFG.defMaxCount; i++) {
    const cloned = skeletonClone(defG.scene);
    cloned.traverse((o) => { if (o.isMesh || o.isSkinnedMesh) o.material = o.material.clone(); });
    const rig = makeRig(cloned, defG.animations.map((a) => a.clone()), CFG.defHeight);
    rig.mixer.timeScale = 0.9 + (i % 5) * 0.06;
    rig.root.visible = false;
    scene.add(rig.root);
    defenders.push({ rig, active: false, type: "chaser", downTimer: 0, staggerTimer: 0, speed: 9, pos: new THREE.Vector3(), radius: CFG.tackleRadius });
  }
  // optional dance emote model
  try {
    const danceG = await loadGLB(ASSETS.heroDance);
    const rig = makeRig(danceG.scene, danceG.animations, CFG.heroHeight);
    rig.root.visible = false;
    scene.add(rig.root);
    heroDance = rig;
    danceAvailable = true;
  } catch (e) { danceAvailable = false; }
  return true;
}

/* ============================== PICKUPS + BOOST PADS */
const pickups = [];
{
  const orbGeo = new THREE.SphereGeometry(0.42, 12, 10);
  const orbMat = new THREE.MeshLambertMaterial({ color: 0x27e0ff, emissive: 0x27e0ff, emissiveIntensity: 0.8 });
  const goldGeo = new THREE.SphereGeometry(0.4, 10, 8);
  const goldMat = new THREE.MeshLambertMaterial({ color: 0xffd34d, emissive: 0xffb300, emissiveIntensity: 0.7 });
  for (let i = 0; i < CFG.orbCount + 1; i++) {
    const isGold = i === CFG.orbCount;
    const mesh = new THREE.Mesh(isGold ? goldGeo : orbGeo, isGold ? goldMat : orbMat);
    if (isGold) mesh.scale.set(1.25, 0.9, 0.9);
    mesh.visible = false;
    scene.add(mesh);
    pickups.push({ mesh, gold: isGold, active: false, phase: i * 2.1 });
  }
}
const boostPads = [];
{
  const padMat = new THREE.MeshLambertMaterial({ color: 0x27e0ff, emissive: 0x27e0ff, emissiveIntensity: 0.5 });
  for (let i = 0; i < CFG.boostPads; i++) {
    const mesh = new THREE.Mesh(new THREE.BoxGeometry(2.2, 0.08, 3.2), padMat);
    mesh.visible = false;
    scene.add(mesh);
    boostPads.push({ mesh, active: false });
  }
}

/* ============================== CONFETTI · one InstancedMesh */
const confetti = {
  mesh: new THREE.InstancedMesh(
    new THREE.PlaneGeometry(0.22, 0.34),
    new THREE.MeshBasicMaterial({ side: THREE.DoubleSide }),
    CFG.confettiMax
  ),
  px: new Float32Array(CFG.confettiMax), py: new Float32Array(CFG.confettiMax), pz: new Float32Array(CFG.confettiMax),
  vx: new Float32Array(CFG.confettiMax), vy: new Float32Array(CFG.confettiMax), vz: new Float32Array(CFG.confettiMax),
  rot: new Float32Array(CFG.confettiMax), rv: new Float32Array(CFG.confettiMax),
  alive: 0,
};
{
  confetti.mesh.visible = false;
  const col = new THREE.Color();
  const crng = mulberry32(99);
  for (let i = 0; i < CFG.confettiMax; i++) {
    col.setHSL(crng(), 0.85, 0.6);
    confetti.mesh.setColorAt(i, col);
  }
  if (confetti.mesh.instanceColor) confetti.mesh.instanceColor.needsUpdate = true;
  scene.add(confetti.mesh);
}
const _dummy = new THREE.Object3D();
function confettiBurst(x, y, z, rng) {
  confetti.alive = CFG.confettiMax;
  confetti.mesh.visible = true;
  for (let i = 0; i < CFG.confettiMax; i++) {
    confetti.px[i] = x + (rng() - 0.5) * 10;
    confetti.py[i] = y + 6 + rng() * 9;
    confetti.pz[i] = z + (rng() - 0.5) * 10;
    confetti.vx[i] = (rng() - 0.5) * 4;
    confetti.vy[i] = -(1.5 + rng() * 2.5);
    confetti.vz[i] = (rng() - 0.5) * 4;
    confetti.rot[i] = rng() * Math.PI;
    confetti.rv[i] = (rng() - 0.5) * 8;
  }
}
function confettiUpdate(dt) {
  if (confetti.alive <= 0) { confetti.mesh.visible = false; return; }
  let live = 0;
  for (let i = 0; i < CFG.confettiMax; i++) {
    if (confetti.py[i] > -1) {
      confetti.px[i] += confetti.vx[i] * dt;
      confetti.py[i] += confetti.vy[i] * dt;
      confetti.pz[i] += confetti.vz[i] * dt;
      confetti.rot[i] += confetti.rv[i] * dt;
      live++;
    }
    _dummy.position.set(confetti.px[i], Math.max(confetti.py[i], -2), confetti.pz[i]);
    _dummy.rotation.set(confetti.rot[i], confetti.rot[i] * 0.7, 0);
    _dummy.scale.setScalar(confetti.py[i] > -1 ? 1 : 0.0001);
    _dummy.updateMatrix();
    confetti.mesh.setMatrixAt(i, _dummy.matrix);
  }
  confetti.mesh.instanceMatrix.needsUpdate = true;
  confetti.alive = live;
}

/* ============================== HUD */
const $ = (id) => document.getElementById(id);
const hud = {
  score: $("vScore"), time: $("vTime"), downs: $("vDowns"), wave: $("vWave"), bestTop: $("vBest"),
  staminaFill: $("staminaFill"), banner: $("banner"), subBanner: $("subBanner"), chainPill: $("chainPill"),
  vignette: $("vignette"), arrowL: $("arrowL"), arrowR: $("arrowR"),
  titleOverlay: $("titleOverlay"), gameoverOverlay: $("gameoverOverlay"), pausedNote: $("pausedNote"),
  loadNote: $("loadNote"), dropPrompt: $("dropPrompt"),
};
const hudCache = { score: -1, time: -1, downs: -1, wave: -1, stamina: -1, chain: -1, best: -1, rank: -1 };
function rankFor(score) {
  return score >= 21 ? 3 : score >= 14 ? 2 : score >= 7 ? 1 : 0;
}
function initStaticText() {
  $("lblScore").textContent = STR.score; $("lblTime").textContent = STR.time;
  $("lblDowns").textContent = STR.downs; $("lblWave").textContent = STR.wave; $("lblBest").textContent = STR.best;
  $("lblRank").textContent = STR.rank; $("vRank").textContent = STR.rankNames[0];
  $("hofTitle").textContent = STR.hallOfFameBoard;
  $("titleH").textContent = STR.title; $("tagline").textContent = STR.tagline;
  $("goalLine").textContent = STR.goal;
  $("ctlKeyboard").textContent = STR.controlsKeyboard;
  $("ctlTouch").textContent = STR.controlsTouch;
  $("ctlPad").textContent = STR.controlsPad;
  hud.dropPrompt.textContent = STR.tapToDrop;
  hud.loadNote.textContent = STR.loading;
  hud.dropPrompt.style.visibility = "hidden";
  $("goScoreLabel").textContent = STR.finalScore; $("goBestLabel").textContent = STR.best;
  $("restartBtn").textContent = STR.playAgain;
  $("shareBtn").textContent = STR.shareChallenge;
  hud.pausedNote.textContent = STR.paused;
  document.title = STR.title;
}
let bannerTimer = 0, subBannerTimer = 0;
function showBanner(text, secs) {
  hud.banner.textContent = text;
  hud.banner.classList.remove("pop");
  void hud.banner.offsetWidth; // restart the pop animation
  hud.banner.classList.add("pop");
  hud.banner.style.opacity = "1";
  bannerTimer = secs;
}
function showSub(text, secs) {
  hud.subBanner.textContent = text;
  hud.subBanner.style.opacity = "1";
  subBannerTimer = secs;
}
function fmtTime(t) {
  const s = Math.max(0, Math.ceil(t));
  return ((s / 60) | 0) + ":" + String(s % 60).padStart(2, "0");
}
function hudUpdate() {
  if (hudCache.score !== state.score) { hudCache.score = state.score; hud.score.textContent = String(state.score); }
  const tSec = Math.max(0, Math.ceil(state.time));
  if (hudCache.time !== tSec) { hudCache.time = tSec; hud.time.textContent = fmtTime(state.time); }
  if (hudCache.downs !== state.downs) {
    hudCache.downs = state.downs;
    hud.downs.textContent = "◆".repeat(Math.max(0, state.downs)) + "◇".repeat(Math.max(0, CFG.downsMax - state.downs));
  }
  if (hudCache.wave !== state.wave) { hudCache.wave = state.wave; hud.wave.textContent = String(state.wave); }
  if (hudCache.best !== state.best) { hudCache.best = state.best; hud.bestTop.textContent = String(state.best); }
  const st = Math.round(state.stamina);
  if (hudCache.stamina !== st) { hudCache.stamina = st; hud.staminaFill.style.width = st + "%"; }
  const rk = rankFor(state.score);
  if (hudCache.rank !== rk) { hudCache.rank = rk; $("vRank").textContent = STR.rankNames[rk]; }
  if (hudCache.chain !== state.chain) {
    hudCache.chain = state.chain;
    if (state.chain >= 2) {
      hud.chainPill.textContent = state.chain >= 3 ? STR.chain3 : STR.chain2;
      hud.chainPill.style.opacity = "1";
    } else {
      hud.chainPill.style.opacity = "0";
    }
  }
}

/* ============================== GAME STATE */
function lsGet(key, fallback) { try { return localStorage.getItem(key) || fallback; } catch (e) { return fallback; } }
function lsSet(key, val) { try { localStorage.setItem(key, val); } catch (e) {} }
const state = {
  mode: "title", // title | drop | run | td | tackled | over
  score: 0, downs: CFG.downsMax, time: CFG.matchTime, wave: 1,
  stamina: CFG.staminaMax, sprintLocked: false,
  px: 0, py: 0, pz: 0, vx: 0, vz: 0, yaw: 0,
  jukeTimer: 0, jukeDir: 0, jukeCdTimer: 0, invulnTimer: 0,
  spinTimer: 0, spinCdTimer: 0, burstTimer: 0,
  chain: 0, chainTimer: 0, styleBonusAtTd: 0,
  streak: 0, hotHand: false, surgeUsed: false,
  modeTimer: 0, tdPhase: 0, orbitAngle: 0, animTime: 0,
  tdilation: 1, dilationTimer: 0,
  matchIndex: 0, rng: mulberry32(0xc0ffee),
  best: Number(lsGet("gridiron_best", "0")),
  nightShown: false, ready: false,
};

function nightAmount() { return Math.min(1, (state.wave - 1) / 4); }
const _colA = new THREE.Color(), _colB = new THREE.Color();
function applyNight() {
  const t = nightAmount();
  sun.intensity = 1.5 - t * 0.95;
  hemi.intensity = 0.9 - t * 0.35;
  _colA.set(0xffe2b0); _colB.set(0x7a86ff); sun.color.copy(_colA.lerp(_colB, t));
  _colA.set(0xc97bd9); _colB.set(0x221345); scene.fog.color.copy(_colA.lerp(_colB, t));
  const dim = 1 - t * 0.55;
  panoMat.color.setScalar(dim);
  skyMat.color.setScalar(dim);
  for (const m of towers) m.emissiveIntensity = t * 2.2;
  if (t >= 0.5 && !state.nightShown) { state.nightShown = true; showSub(STR.nightShow, 2.2); }
}

function startMatch() {
  if (!state.ready) return;
  state.matchIndex++;
  state.rng = mulberry32(0xc0ffee + state.matchIndex * 7919);
  state.score = 0; state.downs = CFG.downsMax; state.time = CFG.matchTime; state.wave = 1;
  state.stamina = CFG.staminaMax; state.sprintLocked = false;
  state.burstTimer = 0; state.chain = 0; state.chainTimer = 0; state.nightShown = false;
  state.streak = 0; state.hotHand = false; state.surgeUsed = false;
  setAmbientLevel(1);
  hud.titleOverlay.style.display = "none";
  hud.gameoverOverlay.style.display = "none";
  audioInit();
  startMusic();
  startAmbient();
  playVo("voWelcome");
  startDrive(true);
}

function startDrive(withDrop) {
  state.px = 0; state.pz = 0; state.vx = 0; state.vz = 0; state.yaw = 0;
  state.jukeTimer = 0; state.jukeCdTimer = 0; state.invulnTimer = 0;
  state.spinTimer = 0; state.spinCdTimer = 0;
  state.chain = 0; state.chainTimer = 0;
  state.tdilation = 1; state.dilationTimer = 0;
  hero.root.rotation.set(0, 0, 0);
  hero.root.visible = true;
  if (heroDance) heroDance.root.visible = false;
  if (hero.runAction) hero.runAction.paused = false;
  applyNight();
  if (withDrop) {
    state.mode = "drop";
    state.py = CFG.dropHeight;
    canopy.visible = true;
  } else {
    state.mode = "run";
    state.py = 0;
    canopy.visible = false;
    playSfx("whistle");
  }
  const count = Math.min(CFG.defBaseCount + state.wave, CFG.defMaxCount);
  const speed = Math.min(CFG.defBaseSpeed + (state.wave - 1) * CFG.defSpeedPerWave, CFG.defSpeedMax);
  for (let i = 0; i < defenders.length; i++) {
    const d = defenders[i];
    d.active = i < count;
    d.rig.root.visible = d.active;
    d.downTimer = 0; d.staggerTimer = 0;
    d.rig.root.rotation.set(0, Math.PI, 0);
    if (!d.active) continue;
    const typeName = state.wave >= 2 && i % 4 === 3 ? "tank" : state.wave >= 3 && i % 3 === 2 ? "blitzer" : "chaser";
    d.type = typeName;
    const T = DEF_TYPES[typeName];
    d.speed = speed * T.speedMult * (0.92 + state.rng() * 0.16);
    d.radius = T.radius;
    d.rig.model.scale.setScalar(d.rig.model.scale.x / (d.baseScale || 1) * 1); // reset chain below
    if (!d.baseScale) d.baseScale = 1;
    d.rig.root.scale.setScalar(T.scale);
    d.rig.model.rotation.x = typeName === "tank" ? 0.14 : 0;
    if (d.rig.runAction) d.rig.runAction.timeScale = T.anim;
    d.rig.model.traverse((o) => { if (o.material && o.material.color) o.material.color.setHex(T.tint); });
    // drop-in drives land around z 13-26: keep the landing zone clear so the first read is fair
    const zMin = withDrop ? 32 : 14;
    d.pos.set((state.rng() - 0.5) * (CFG.fieldW - 6), 0, zMin + state.rng() * (CFG.driveLen - zMin - 10));
  }
  for (const p of pickups) {
    p.active = p.gold ? state.rng() < CFG.goldChance : true;
    p.mesh.visible = p.active;
    if (p.active) p.mesh.position.set((state.rng() - 0.5) * (CFG.fieldW - 8), 0.9, 12 + state.rng() * (CFG.driveLen - 20));
  }
  for (const b of boostPads) {
    b.active = true;
    b.mesh.visible = true;
    b.mesh.position.set((state.rng() - 0.5) * (CFG.fieldW - 10), 0.05, 16 + state.rng() * (CFG.driveLen - 28));
  }
}

function clutchMult() {
  const lost = CFG.downsMax - state.downs;
  let m = 1 + lost * CFG.clutchPerDown;
  if (state.burstTimer > 0) m *= CFG.burstMult;
  if (state.hotHand) m *= 1.08; // hot hand is a real buff, not a label
  return m;
}

function bumpChain() {
  state.chain = Math.min(3, state.chain + 1);
  state.chainTimer = CFG.chainWindow;
  if (state.chain === 2) showSub(STR.chain2, 1.4);
  if (state.chain === 3) showSub(STR.chain3, 1.8);
  hud.vignette.style.opacity = "1";
}

function touchdown() {
  const prevScore = state.score, prevRank = rankFor(prevScore);
  state.styleBonusAtTd = CFG.chainBonus[state.chain] || 0;
  state.score += CFG.tdPoints + state.styleBonusAtTd;
  state.wave++;
  state.mode = "td";
  state.tdPhase = 0;
  state.modeTimer = 0.7;
  state.tdilation = 0.35;
  state.dilationTimer = 0;
  // status beats (OS_PULL_V2 P8/P10/P13): rank up, hot hand, hidden surge, withhold then reveal
  const crossedMvp = prevScore < CFG.mvpScore && state.score >= CFG.mvpScore;
  showBanner(crossedMvp ? STR.mvp : STR.touchdown, crossedMvp ? 2.6 : 2.0);
  if (state.styleBonusAtTd > 0) showSub(STR.styleBonus + " +" + state.styleBonusAtTd, 2.0);
  state.streak++;
  if (state.streak >= 2 && !state.hotHand) {
    state.hotHand = true;
    showSub(STR.hotHand, 2.0);
    playVo(audio.buffers.voHothand ? "voHothand" : "voTouchdown");
  } else if (crossedMvp) {
    playVo("voMvp");
  } else {
    playVo("voTouchdown");
  }
  if (!state.surgeUsed && state.chain >= 2) {
    state.surgeUsed = true;
    state.stamina = CFG.staminaMax;
    state.burstTimer = 3;
    showSub(STR.crowdSurge, 2.2);
  }
  const newRank = rankFor(state.score);
  if (newRank > prevRank && !crossedMvp) showSub(STR.rankUp.replace("{rank}", STR.rankNames[newRank]), 2.2);
  if (state.score >= 14 && state.score < CFG.mvpScore) setAmbientLevel(0.6);
  if (crossedMvp) setAmbientLevel(1.7);
  playSfx("touchdown", crossedMvp ? 1.0 : 0.8);
  confettiBurst(state.px, 0, state.pz, state.rng);
}

function tackled() {
  state.downs--;
  state.mode = "tackled";
  state.modeTimer = 1.5;
  state.chain = 0;
  if (state.hotHand) { state.hotHand = false; showSub(STR.hotHandLost, 1.6); }
  state.streak = 0;
  playSfx("tackle");
  if (state.downs === 1) {
    showBanner(STR.tackled, 1.2);
    playVo("voLastdown");
    showSub(STR.lastDown, 2.0);
  } else {
    showBanner(STR.tackled, 1.2);
  }
}

function endMatch(reason) {
  state.mode = "over";
  state.modeTimer = 1.2;
  state.tdilation = 1;
  const prevBest = state.best;
  if (state.score > state.best) {
    state.best = state.score;
    lsSet("gridiron_best", String(state.best));
  }
  const isMvp = state.score >= CFG.mvpScore;
  const newBest = state.score > 0 && state.score > prevBest;
  const goTitle = $("goTitle");
  goTitle.textContent = isMvp ? STR.mvp : STR.title;
  goTitle.classList.toggle("mvp", isMvp);
  const headline = isMvp ? STR.endHeadlineMvp
    : newBest ? STR.endHeadlineNewBest
    : STR.endHeadlineBeatBest.replace("{best}", String(state.best));
  $("goReason").textContent = reason + " · " + headline;
  $("goScore").textContent = String(state.score);
  $("goBest").textContent = String(state.best);
  // hall of fame board: local top 5, no RNG, earned only (OS_PULL_V2 P10)
  hud.gameoverOverlay.style.display = "flex";
  let hof = [];
  try { hof = JSON.parse(lsGet("gridiron_hof", "[]")); } catch (e) { hof = []; }
  hof.push({ s: state.score, mvp: isMvp });
  hof.sort((a, b) => b.s - a.s);
  hof = hof.slice(0, 5);
  lsSet("gridiron_hof", JSON.stringify(hof));
  $("hofList").textContent = hof.map((h, i) => (i + 1) + ". " + h.s + (h.mvp ? " · " + STR.mvp : "")).join("   ");
  if (reason === STR.gameOverDowns) playVo(audio.buffers.voTurnover ? "voTurnover" : "voLastdown");
  if (isMvp) { confettiBurst(state.px, 0, state.pz, state.rng); playVo("voMvp"); }
}
$("restartBtn").addEventListener("click", () => { if (state.mode === "over") startMatch(); });
for (const id of ["restartBtn", "shareBtn"]) {
  document.getElementById(id).addEventListener("pointerdown", (e) => e.stopPropagation());
}
$("shareBtn").addEventListener("click", () => {
  const tpl = state.score >= CFG.mvpScore ? STR.shareTextMvp : STR.shareText;
  const text = tpl.replace("{score}", String(state.score)) + " " + location.href;
  const btn = $("shareBtn");
  const done = () => { btn.textContent = STR.shareCopied; setTimeout(() => { btn.textContent = STR.shareChallenge; }, 1600); };
  if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, done);
  else done();
});

/* ============================== SIM UPDATE (fixed 60 Hz; dt scaled by tdilation for slow-mo beats) */
const prevCmd = { jukeL: false, jukeR: false, spin: false };
function nearestThreatDist() {
  let best = 1e9;
  for (const d of defenders) {
    if (!d.active || d.downTimer > 0) continue;
    const dx = d.pos.x - state.px, dz = d.pos.z - state.pz;
    const dist2 = dx * dx + dz * dz;
    if (dist2 < best) best = dist2;
  }
  return Math.sqrt(best);
}
function update(rawMs) {
  const dt = (rawMs / 1000) * state.tdilation;
  const c = readCommands();
  state.animTime += dt;

  if (bannerTimer > 0) { bannerTimer -= dt; if (bannerTimer <= 0) hud.banner.style.opacity = "0"; }
  if (subBannerTimer > 0) { subBannerTimer -= dt; if (subBannerTimer <= 0) hud.subBanner.style.opacity = "0"; }
  if (state.dilationTimer > 0) { state.dilationTimer -= rawMs / 1000; if (state.dilationTimer <= 0) state.tdilation = 1; }
  if (state.chainTimer > 0) { state.chainTimer -= dt; if (state.chainTimer <= 0) state.chain = 0; }
  if (hud.vignette.style.opacity === "1" && state.jukeTimer <= 0 && state.spinTimer <= 0) hud.vignette.style.opacity = "0";

  if (state.mode === "title") {
    if (c.any) startMatch();
    prevCmd.jukeL = c.jukeL; prevCmd.jukeR = c.jukeR; prevCmd.spin = c.spin;
    return;
  }
  if (state.mode === "over") {
    confettiUpdate(dt);
    state.modeTimer -= dt;
    if (state.modeTimer <= 0 && c.any) startMatch();
    prevCmd.jukeL = c.jukeL; prevCmd.jukeR = c.jukeR; prevCmd.spin = c.spin;
    return;
  }

  if (state.mode === "drop") {
    state.py -= CFG.dropFall * dt;
    state.px = clampX(state.px + c.x * 9 * dt);
    state.pz += (4 + c.z * 4) * dt;
    hero.root.rotation.z = -c.x * 0.35;
    if (state.py <= 0) {
      state.py = 0;
      state.mode = "run";
      canopy.visible = false;
      hero.root.rotation.z = 0;
      state.invulnTimer = 1.0; // landing grace
      playSfx("whistle");
    }
  } else if (state.mode === "run") {
    state.time -= dt;
    if (state.time <= 0) { state.time = 0; endMatch(STR.gameOverClock); return; }

    const wantSprint = c.sprint && c.z > 0.1;
    if (state.sprintLocked && state.stamina > CFG.staminaGate) state.sprintLocked = false;
    const sprinting = wantSprint && !state.sprintLocked && state.stamina > 0;
    if (sprinting) {
      state.stamina -= CFG.staminaDrain * dt;
      if (state.stamina <= 0) { state.stamina = 0; state.sprintLocked = true; }
    } else {
      state.stamina = Math.min(CFG.staminaMax, state.stamina + CFG.staminaRegen * dt);
    }

    if (state.jukeCdTimer > 0) state.jukeCdTimer -= dt;
    if (state.spinCdTimer > 0) state.spinCdTimer -= dt;
    if (state.invulnTimer > 0) state.invulnTimer -= dt;
    if (state.burstTimer > 0) state.burstTimer -= dt;

    if (state.jukeCdTimer <= 0 && state.jukeTimer <= 0) {
      if (c.jukeL && !prevCmd.jukeL) startJuke(-1);
      else if (c.jukeR && !prevCmd.jukeR) startJuke(1);
    }
    if (c.spin && !prevCmd.spin && state.spinCdTimer <= 0) {
      state.spinTimer = CFG.spinTime;
      state.spinCdTimer = CFG.spinCd;
      playSfx("juke");
      if (nearestThreatDist() < CFG.chainNearDist) bumpChain();
    }
    if (state.spinTimer > 0) state.spinTimer -= dt;
    if (state.jukeTimer > 0) state.jukeTimer -= dt;

    const mult = clutchMult();
    const speed = (sprinting ? CFG.sprintSpeed : CFG.baseSpeed) * mult;
    let vx = c.x * speed * 0.85;
    let vz = c.z >= 0 ? c.z * speed : c.z * speed * CFG.backPedal;
    if (state.jukeTimer > 0) vx += state.jukeDir * CFG.jukeDash * (state.jukeTimer / CFG.jukeTime);
    state.vx = vx; state.vz = vz;
    state.px = clampX(state.px + vx * dt);
    state.pz = Math.max(-CFG.endzoneLen + 2, state.pz + vz * dt);

    const spd = Math.hypot(vx, vz);
    if (spd > 0.5) {
      const targetYaw = Math.atan2(vx, vz);
      let dy = targetYaw - state.yaw;
      while (dy > Math.PI) dy -= 2 * Math.PI;
      while (dy < -Math.PI) dy += 2 * Math.PI;
      state.yaw += dy * Math.min(1, dt * 10);
    }

    for (const p of pickups) {
      if (!p.active) continue;
      const dx = p.mesh.position.x - state.px, dz = p.mesh.position.z - state.pz;
      if (dx * dx + dz * dz < 2.25) {
        p.active = false; p.mesh.visible = false;
        if (p.gold) {
          state.score += CFG.goldPoints;
          state.burstTimer = CFG.burstTime;
          showBanner(STR.goldenBall, 1.4);
          if (audio.buffers.voGoldenball) playVo("voGoldenball");
        } else {
          state.stamina = Math.min(CFG.staminaMax, state.stamina + CFG.orbStamina);
        }
        playSfx("pickup");
      }
    }
    for (const b of boostPads) {
      if (!b.active) continue;
      const dx = b.mesh.position.x - state.px, dz = b.mesh.position.z - state.pz;
      if (Math.abs(dx) < 1.4 && Math.abs(dz) < 1.9) {
        b.active = false; b.mesh.visible = false;
        state.burstTimer = CFG.burstTime;
        showSub(STR.boostPad, 1.0);
        playSfx("pickup");
      }
    }

    updateDefenders(dt);
    if (state.mode === "run" && state.pz >= CFG.driveLen) touchdown();
  } else if (state.mode === "td") {
    state.modeTimer -= dt;
    if (state.tdPhase === 0 && state.modeTimer <= 0) {
      state.tdPhase = 1;
      state.modeTimer = 2.6;
      state.tdilation = 1;
      state.orbitAngle = Math.PI;
      // swap in the dance emote model when it exists
      if (danceAvailable && heroDance) {
        hero.root.visible = false;
        heroDance.root.position.set(state.px, 0, state.pz);
        heroDance.root.rotation.y = state.yaw + Math.PI; // face the chasing camera
        heroDance.root.visible = true;
      }
    } else if (state.tdPhase === 1 && state.modeTimer <= 0) {
      startDrive(false);
    }
  } else if (state.mode === "tackled") {
    state.modeTimer -= dt;
    if (state.modeTimer <= 0) {
      if (state.downs <= 0) { endMatch(STR.gameOverDowns); }
      else {
        if (CFG.downsMax - state.downs > 0) showSub(STR.clutch, 1.2);
        startDrive(false);
      }
    }
  }

  confettiUpdate(dt);
  prevCmd.jukeL = c.jukeL; prevCmd.jukeR = c.jukeR; prevCmd.spin = c.spin;
}
function clampX(x) {
  const lim = CFG.fieldW / 2 - 1;
  return Math.max(-lim, Math.min(lim, x));
}
function startJuke(dir) {
  state.jukeTimer = CFG.jukeTime;
  state.jukeDir = dir;
  state.jukeCdTimer = CFG.jukeCd;
  state.invulnTimer = CFG.jukeInvuln;
  state.tdilation = 0.65;
  state.dilationTimer = 0.3;
  playSfx("juke");
  if (nearestThreatDist() < CFG.chainNearDist) bumpChain();
}

function updateDefenders(dt) {
  let warnL = false, warnR = false;
  for (const d of defenders) {
    if (!d.active) continue;
    if (d.downTimer > 0) {
      d.downTimer -= dt;
      d.rig.root.rotation.x = Math.min(d.rig.root.rotation.x + dt * 6, Math.PI / 2);
      if (d.downTimer <= 0) d.rig.root.rotation.x = 0;
      continue;
    }
    if (d.staggerTimer > 0) d.staggerTimer -= dt;
    const effSpeed = d.staggerTimer > 0 ? d.speed * 0.2 : d.speed;
    const dist = Math.hypot(state.px - d.pos.x, state.pz - d.pos.z);
    const leadFactor = d.type === "blitzer" ? 1.0 : 0.6;
    const lead = Math.min(dist / Math.max(d.speed, 1), 1.2) * leadFactor;
    const tx = clampX(state.px + state.vx * lead);
    const tz = state.pz + state.vz * lead;
    let dirx = tx - d.pos.x, dirz = tz - d.pos.z;
    const len = Math.hypot(dirx, dirz) || 1;
    dirx /= len; dirz /= len;
    d.pos.x = clampX(d.pos.x + dirx * effSpeed * dt);
    d.pos.z += dirz * effSpeed * dt;

    if (d.pos.z < state.pz - CFG.defRecycleBehind) {
      d.pos.z = state.pz + 18 + state.rng() * 30;
      d.pos.x = (state.rng() - 0.5) * (CFG.fieldW - 6);
      if (d.pos.z > CFG.driveLen + 6) d.pos.z = CFG.driveLen + 6;
    }

    if (dist < CFG.spinRadius && state.spinTimer > 0) {
      if (d.type === "tank") {
        d.staggerTimer = 1.0;
      } else {
        d.downTimer = CFG.defKnockTime;
        playSfx("tackle", 0.5);
      }
      continue;
    }
    if (dist < d.radius && state.invulnTimer <= 0 && state.mode === "run") {
      tackled();
    }

    if (d.pos.z < state.pz - 1 && state.pz - d.pos.z < 8 && Math.abs(d.pos.x - state.px) < 6) {
      if (d.pos.x < state.px) warnL = true; else warnR = true;
    }
  }
  if (warnL !== lastWarnL) { lastWarnL = warnL; hud.arrowL.style.opacity = warnL ? "1" : "0"; }
  if (warnR !== lastWarnR) { lastWarnR = warnR; hud.arrowR.style.opacity = warnR ? "1" : "0"; }
}
let lastWarnL = false, lastWarnR = false;

/* ============================== RENDER */
const _v1 = new THREE.Vector3();
const _v2 = new THREE.Vector3();
let camRoll = 0;
function render(dtReal) {
  if (!state.ready) { renderer.render(scene, camera); return; }

  hero.root.position.set(state.px, state.py, state.pz);
  hero.root.rotation.y = state.yaw;
  if (state.spinTimer > 0) {
    hero.root.rotation.y = state.yaw + (1 - state.spinTimer / CFG.spinTime) * Math.PI * 2;
  }
  if (state.mode === "tackled") {
    hero.root.rotation.x = Math.min(hero.root.rotation.x + 0.12, Math.PI / 2.2);
  } else if (state.mode !== "over") {
    hero.root.rotation.x = 0;
  }

  // animation mixers: run speed follows actual velocity
  const spd = Math.hypot(state.vx, state.vz);
  if (hero.runAction) {
    if (state.mode === "drop") hero.runAction.timeScale = 0.35;
    else if (state.mode === "tackled") hero.runAction.timeScale = 0;
    else hero.runAction.timeScale = Math.max(0.25, (spd / CFG.baseSpeed) * 1.05);
  }
  hero.mixer.update(dtReal * state.tdilation);
  if (heroDance && heroDance.root.visible) heroDance.mixer.update(dtReal);

  for (const d of defenders) {
    if (!d.active) continue;
    d.rig.root.position.set(d.pos.x, 0, d.pos.z);
    if (d.downTimer <= 0) {
      d.rig.root.rotation.y = Math.atan2(state.px - d.pos.x, state.pz - d.pos.z);
      d.rig.mixer.update(dtReal * state.tdilation);
    }
  }

  // football follows the hand bone (fallback: hip-height offset beside the hero)
  if (ballMesh) {
    if (ballBone) {
      ballBone.getWorldPosition(_v2);
      ballMesh.position.copy(_v2);
    } else {
      ballMesh.position.set(state.px + Math.cos(state.yaw) * 0.45, state.py + 1.0, state.pz - Math.sin(state.yaw) * 0.45);
    }
    ballMesh.rotation.y = state.yaw;
    ballMesh.visible = hero.root.visible;
  }

  for (const p of pickups) {
    if (!p.active) continue;
    p.mesh.position.y = 0.9 + Math.sin(state.animTime * 2.2 + p.phase) * 0.18;
    p.mesh.rotation.y += 0.03;
  }
  for (let i = 0; i < islands.length; i++) {
    const g = islands[i];
    g.position.y = g.userData.baseY + Math.sin(state.animTime * 0.5 + g.userData.phase) * 1.2;
  }

  // camera
  let targetFov = 58;
  if (state.mode === "td" && state.tdPhase === 1) {
    state.orbitAngle += dtReal * 1.5;
    const r = 6.5;
    camera.position.set(
      state.px + Math.sin(state.orbitAngle) * r,
      2.8,
      state.pz + Math.cos(state.orbitAngle) * r
    );
    _v1.set(state.px, 1.3, state.pz);
    camera.lookAt(_v1);
  } else {
    let cy, cz, ly;
    if (state.mode === "drop") { cy = state.py + 6; cz = state.pz - 14; ly = state.py; }
    else { cy = 7.6; cz = state.pz - 12.5; ly = 1.7; }
    camera.position.x += (state.px * 0.6 - camera.position.x) * 0.08;
    camera.position.y += (cy - camera.position.y) * 0.08;
    camera.position.z += (cz - camera.position.z) * 0.12;
    _v1.set(state.px, ly, state.pz + 7);
    camera.lookAt(_v1);
    if (spd > CFG.baseSpeed * 1.1) targetFov = 66;
    const targetRoll = state.jukeTimer > 0 ? -state.jukeDir * 0.06 : 0;
    camRoll += (targetRoll - camRoll) * 0.2;
    camera.rotateZ(camRoll);
  }
  camera.fov += (targetFov - camera.fov) * 0.08;
  camera.updateProjectionMatrix();
  sky.position.z = state.pz;
  panoCyl.position.z = state.pz;
  panoCyl.rotation.y = state.animTime * 0.004; // slow drift keeps the horizon alive

  hudUpdate();
  renderer.render(scene, camera);
}

/* ============================== LOOP · fixed timestep, pause on blur */
const STEP = 1000 / 60;
let acc = 0, last = performance.now(), paused = false, frames = 0, fpsAt = last;
addEventListener("blur", () => {
  paused = true; hud.pausedNote.style.display = "block";
  held.clear();
  touchState.sprint = touchState.jukeL = touchState.jukeR = touchState.spin = false;
});
addEventListener("focus", () => { paused = false; last = performance.now(); hud.pausedNote.style.display = "none"; });
const qs = new URLSearchParams(location.search);
const dev = qs.has("dev");
const selftest = qs.has("selftest"); // dev probe: auto-start, skip the drop
if (dev) document.getElementById("dev").style.display = "block";
const devEl = document.getElementById("dev");

function frame(now) {
  requestAnimationFrame(frame);
  if (paused) return;
  const frameMs = now - last;
  acc += frameMs; last = now;
  if (acc > 250) acc = 250;
  while (acc >= STEP) { update(STEP); acc -= STEP; }
  render(Math.min(frameMs, 100) / 1000);
  if (dev) {
    frames++;
    if (now - fpsAt >= 500) {
      const fps = Math.round((frames * 1000) / (now - fpsAt));
      frames = 0; fpsAt = now;
      devEl.textContent = fps + " fps · calls " + renderer.info.render.calls + " · tris " + renderer.info.render.triangles;
    }
  }
}

bootMark("module-end");
initStaticText();
requestAnimationFrame(frame);
bootAssets().then(() => {
  state.ready = true;
  bootMark(danceAvailable ? "ready-dance" : "ready");
  hud.loadNote.textContent = "";
  hud.dropPrompt.style.visibility = "visible";
  if (selftest) {
    startMatch(); state.mode = "run"; state.py = 0; canopy.visible = false;
    window.__gr = state; // probe hook, selftest only
  }
}).catch((err) => {
  bootMark("assets-failed");
  hud.loadNote.textContent = STR.bootError.replace("{msg}", String(err && err.message || err));
});
