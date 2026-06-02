---
name: epms-site-analysis
description: |
  Assesses data center Electrical Power Monitoring Systems by evaluating the three-layer architecture (Field, Communication, Application) and six-tier monitoring node hierarchy.
  Use when:
  - analyzing a data center's power monitoring capabilities
  - commissioning or auditing EPMS systems for a new or existing facility
  - identifying metering gaps across the power distribution chain
  - verifying communication paths from field meters to EPMS server
  - cross-referencing EPMS coverage with electrical, mechanical, and fire protection systems
  - assessing compliance with 2N redundancy standards
  Keywords: EPMS, data center, power monitoring, metering, power quality, Modbus, SCADA, three-layer architecture, monitoring nodes, power distribution, ION meters
---

# EPMS Site Analysis (Three-Layer Assessment)

**Skill ID:** 21.1  
**Category:** Data Center Engineering (EPMS)  
**Source Document(s):** EPMS_Universal_Framework.docx, 01_Electrical_Power_System.docx, 02_Mechanical_Cooling_System.docx, 03_Fire_Protection_System.docx, 04_Site_Infrastructure.docx

## Purpose

Assess any data center's Electrical Power Monitoring System by evaluating the three-layer architecture (Field, Communication, Application) and the six-tier monitoring node hierarchy to identify metering gaps and operational risks.

## When to Use

When crafting any business communication that needs to be clear, memorable, and drive action.

## Instructions

Follow this workflow precisely. Each step is grounded in the source document(s) listed above. Do not skip steps. Do not invent frameworks, models, or terminology not present in the source material. Execute each step in order, using the exact logic and decision criteria documented.

## Workflow

1. Assess Field Layer: Verify power quality meters are installed at each distribution tier. Check meter types against tier requirements (Tier 1 Utility/MV = ION-9000/ION-7650, Tier 2 Generator = ION-9000/PM8000, through Tier 6 IT PDU = inline meters).
2. Document metering gaps: Not all sites meter every tier. Record which tiers are unmetered and the business risk this creates (e.g., no Tier 4 UPS output metering = blind to UPS efficiency and battery state).
3. Assess Communication Layer: Verify RS-485/Modbus field connections, segment converters (RS-485 to TCP/IP), managed network switches, and SCADA/EPMS server connectivity. Check for max device limits per RS-485 segment (~32).
4. Assess Application Layer: Verify EPMS server/software functionality including historian data retention, alarming configuration, dashboard quality, and integration with BMS/DCIM.
5. Cross-reference electrical, mechanical, and fire protection systems: Verify EPMS visibility into UPS status, chiller plant performance, CRAH operation, generator synchronization, and fire suppression system coordination.
6. Check for data center standard architecture compliance: 2N redundancy at every tier, dual MV feeders, dual UPS (A/B paths), dual STS, dual PDU distribution chains.
7. Compile findings into a gap analysis with risk ratings and remediation priorities.

## Output Format

Produce all of the following deliverables:

- A three-layer EPMS architecture assessment (Field, Communication, Application)
- A six-tier metering coverage matrix with gap identification
- A communication path diagram showing meter-to-server connectivity
- A gap analysis with risk ratings and remediation priority list

## Example Use

User provides context about their specific situation. The skill guides them through each workflow step sequentially, producing all deliverables listed in the Output Format section. Each step builds on the previous one, and no step should be skipped.
