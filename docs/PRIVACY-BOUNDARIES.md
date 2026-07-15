# Privacy Boundaries

Public portfolio content must never expose company, client, employee, tenant, authentication, or production infrastructure secrets.

## Tekfen Construction

**Allowed**

- Job title: IT Specialist — Tekfen Construction
- High-level description of enterprise/industrial IT support work
- Generically framed skills gained (Windows, networking, troubleshooting)

**Not allowed**

- Internal tickets, hostnames, IPs, diagrams of client networks
- Credentials, VPN details, asset inventories from work systems
- Screenshots of production consoles or mailboxes
- Employee or contractor directories
- Confidential process documents

## Saudi Aramco project environment

**Correct wording**

> Supporting enterprise IT operations within a Tekfen Construction environment associated with Saudi Aramco projects.

**Not allowed**

- Claiming employment by Saudi Aramco
- Publishing Aramco systems, policies, configurations, or findings
- Naming restricted sites, projects, or systems beyond the approved phrasing

## Crow Ecosystem

**Allowed**

- Public architecture summaries already present in the public repository
- Stack names (Next.js, Prisma, Supabase, Vercel, etc.)
- Links to the public repository

**Not allowed**

- Authentication secrets, database URLs, service role keys
- Tenant identifiers, client names, private security findings
- Internal bypass details or unpublished vulnerability notes
- Duplicating private branches or credentials into other repos

## Enterprise cybersecurity lab

**Allowed**

- Lab names such as `lab.local`, `SRV-01`, `KALI-01` when they are personal lab labels
- Architecture diagrams without production mapping
- Hardening checklists and detection *exercise* outlines

**Not allowed**

- Real passwords, API keys, or reusable secrets
- Unnecessary private IP publication
- Destructive exploit playbooks
- Mapping lab hosts to employer networks

## University / SecSky

- Publish contribution and achievement wording only when accurate
- Mark unverified technical claims as **To Be Verified**
- Do not publish teammate personal data without consent
- Clarify ownership before licensing team source code

## Smart Methods / robotics

- Document participation concepts without publishing company IP
- Do not claim ownership of Smart Methods materials

## Personal information

**Public contact allowed:** GitHub, LinkedIn, professional email

**Require owner approval:** phone number, personal photo, home address, family data

## Secret management

Before any public push:

1. Scan for tokens, keys, `.env`, certificates, connection strings
2. Prefer generated/sample data in examples
3. Keep company material offline
4. Use GitHub secret scanning where available
5. Remove or rotate anything accidentally committed

## Screenshot sanitation

Blur or remove: emails not meant for publication, internal hostnames, tokens, sensitive IPs, client/employee names, tenant IDs, private paths, production logs.
