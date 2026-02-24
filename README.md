# QR Doorbell Platform (No-App Visitor Contact)

This repository contains a practical starter plan to build a **QR-based doorbell replacement** where:
- each resident has a unique QR code at their door,
- any visitor can scan and contact the resident with **text, voice note, or live video**,
- visitors do **not** need to install an app or sign up,
- residents/service providers use a secure app/dashboard.

## What this solves
Traditional doorbells fail when residents are away or in another room. This platform lets visitors contact the resident instantly through browser-based communication.

## Core user journeys
1. **Resident onboarding (app/dashboard)**
   - Resident signs up, verifies phone/email, creates profile.
   - System generates a unique QR code and printable door card.

2. **Visitor contact (no app, no signup)**
   - Visitor scans QR code.
   - Opens resident-specific web page.
   - Chooses **Text Chat**, **Live Video Call**, or **Leave Voice Message**.

3. **Resident receives communication**
   - Push notification in mobile app/web app.
   - Can answer by chat/video or review voice message later.

## Suggested MVP scope
- QR code generation + printable cards
- Visitor web page with contact options
- Real-time text chat (WebSocket)
- Voice message recording and playback
- Optional one-tap video call (WebRTC)
- Resident app/dashboard notifications and history

See the `docs/` folder for:
- complete product and architecture blueprint,
- MVP milestone plan,
- feature ideas to compete with existing apps,
- launch and growth recommendations.

## Repository structure
- `docs/PRODUCT_PLAN.md` — business + product vision, personas, monetization
- `docs/TECH_ARCHITECTURE.md` — stack, schema, APIs, security, infra
- `docs/MVP_BACKLOG.md` — implementation phases and detailed tasks
- `docs/COMPETITIVE_FEATURES.md` — differentiators and growth features

## Recommended first implementation stack
- **Frontend visitor portal**: Next.js (web, mobile-friendly)
- **Resident app**: React Native (single codebase iOS/Android)
- **Backend**: NestJS or FastAPI
- **Database**: PostgreSQL
- **Realtime**: WebSockets (chat/status), WebRTC (video)
- **Storage**: S3-compatible object storage for voice clips
- **Notifications**: Firebase Cloud Messaging + APNs

## Next step for you (non-technical founder)
Start with a 4-week MVP:
1. Finalize branding + pricing assumptions.
2. Build visitor scan-to-chat + voice-note flow first.
3. Add resident app notifications.
4. Test with 10-20 homes before scaling to apartment buildings.
