#!/usr/bin/env python3
"""
os_face.py , face geometry utilities (cv2 Haar cascades).

Shared by the mark-injection (landmark-based placement) and the face-match gate
(aligned face crops). Honest scope: Haar cascades give a face box + eye boxes,
enough for deterministic mole placement and aligned crops. This is NOT a face
EMBEDDING / recognition model , identity matching stays vision-assisted.

CLI:
  detect <img>                 print face box + eye boxes
  anchor <img>                 print the inner-left-eye mole anchor (x,y)
  facecrop <img> --out PNG     write an aligned grayscale face crop (for SSIM)
"""
import os, sys, argparse

def _cv2():
    import cv2
    return cv2


def detect_face(path):
    """Return (x,y,w,h) of the largest detected face, or None."""
    cv2 = _cv2()
    img = cv2.imread(path)
    if img is None:
        return None
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cas = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = cas.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(80, 80))
    if len(faces) == 0:
        return None
    return tuple(int(v) for v in max(faces, key=lambda f: f[2] * f[3]))


def detect_eyes(path):
    """Return list of (x,y,w,h) eye boxes in image coords (within the face ROI)."""
    cv2 = _cv2()
    face = detect_face(path)
    if face is None:
        return []
    fx, fy, fw, fh = face
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # eyes live in the upper ~60% of the face
    roi = gray[fy:fy + int(fh * 0.6), fx:fx + fw]
    cas = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
    eyes = cas.detectMultiScale(roi, scaleFactor=1.1, minNeighbors=6, minSize=(int(fw * 0.12), int(fw * 0.12)))
    return [(int(fx + ex), int(fy + ey), int(ew), int(eh)) for (ex, ey, ew, eh) in eyes]


def inner_left_eye_anchor(path):
    """Mole anchor: below the inner corner of the SUBJECT's left eye
    (= the eye on the RIGHT half of the image). Returns (x,y) or None."""
    eyes = detect_eyes(path)
    if len(eyes) < 1:
        return None
    eyes = sorted(eyes, key=lambda e: e[0])
    # subject's left eye = rightmost eye box in the image
    ex, ey, ew, eh = eyes[-1]
    inner_x = ex + int(ew * 0.18)          # nasal (inner) side of that eye
    below_y = ey + eh + int(eh * 0.35)     # just below the eye, on the cheek
    return (inner_x, below_y)


def aligned_face_crop(path, size=160):
    """Return a size x size grayscale numpy array of the face (for SSIM), or None."""
    import numpy as np
    cv2 = _cv2()
    face = detect_face(path)
    img = cv2.imread(path)
    if img is None:
        return None
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if face is None:
        # fall back to a center crop so the gate can still run (flagged by caller)
        h, w = gray.shape
        s = min(h, w)
        y0, x0 = (h - s) // 2, (w - s) // 2
        crop = gray[y0:y0 + s, x0:x0 + s]
    else:
        x, y, w, h = face
        m = int(0.15 * w)
        y0, y1 = max(0, y - m), min(gray.shape[0], y + h + m)
        x0, x1 = max(0, x - m), min(gray.shape[1], x + w + m)
        crop = gray[y0:y1, x0:x1]
    return cv2.resize(crop, (size, size), interpolation=cv2.INTER_AREA)


def cmd_detect(a):
    f = detect_face(a.img); eyes = detect_eyes(a.img)
    print(f"  face: {f}")
    print(f"  eyes: {eyes}")
    return 0 if f else 1


def cmd_anchor(a):
    p = inner_left_eye_anchor(a.img)
    if p is None:
        print("  no eye anchor found (no face/eyes detected)"); return 1
    print(f"  inner_left_eye anchor (x,y) = {p[0]},{p[1]}")
    return 0


def cmd_facecrop(a):
    import numpy as np
    cv2 = _cv2()
    arr = aligned_face_crop(a.img)
    if arr is None:
        print("  could not crop"); return 1
    cv2.imwrite(a.out, arr)
    print(f"  wrote aligned face crop -> {a.out} (face {'detected' if detect_face(a.img) else 'NOT detected, center fallback'})")
    return 0


def main():
    p = argparse.ArgumentParser(prog="os_face.py")
    sub = p.add_subparsers(dest="cmd")
    d = sub.add_parser("detect"); d.add_argument("img")
    an = sub.add_parser("anchor"); an.add_argument("img")
    fc = sub.add_parser("facecrop"); fc.add_argument("img"); fc.add_argument("--out", required=True)
    a = p.parse_args()
    if a.cmd == "detect": return cmd_detect(a)
    if a.cmd == "anchor": return cmd_anchor(a)
    if a.cmd == "facecrop": return cmd_facecrop(a)
    p.print_help(); return 1


if __name__ == "__main__":
    sys.exit(main())
