# Technical Architecture Blueprint

## 1) High-level components
1. **Visitor Web App (PWA)**
   - Opens from QR scan.
   - Handles text chat, voice recording, optional video call.

2. **Resident App + Web Dashboard**
   - Receives alerts and responds in real-time.
   - Manages profile, availability, and communication settings.

3. **Backend API + Realtime Gateway**
   - Authentication, resident data, conversation records.
   - WebSocket events and signaling for WebRTC calls.

4. **Media + Notification Services**
   - Voice message storage.
   - Push notifications and optional SMS fallback.

## 2) Suggested stack
- **Frontend**: Next.js + Tailwind CSS
- **Mobile app**: React Native + Expo
- **Backend**: NestJS + TypeScript
- **Database**: PostgreSQL + Prisma
- **Cache/Queue**: Redis + BullMQ
- **Storage**: AWS S3 (or Cloudflare R2)
- **Video**: WebRTC (self-hosted signaling or Twilio/Vonage)
- **Monitoring**: Sentry + Prometheus/Grafana

## 3) Data model (starter)
- `users` (resident/service accounts)
- `households` (address + plan)
- `door_profiles` (public slug, QR token, greeting)
- `conversations` (status, started_at, closed_at)
- `messages` (text, sender_role, timestamps)
- `voice_messages` (file_url, duration, transcription)
- `calls` (session metadata, outcome)
- `notification_events` (delivery attempts, channel)

## 4) API outline
- `POST /auth/register`
- `POST /auth/login`
- `GET /door/:slug` (public visitor profile)
- `POST /door/:slug/conversations`
- `POST /conversations/:id/messages`
- `POST /conversations/:id/voice`
- `POST /conversations/:id/call/start`
- `POST /notifications/test`

## 5) Security requirements
- JWT auth for resident endpoints.
- Signed URLs for media uploads/downloads.
- Rate limits and bot prevention on visitor endpoints.
- End-to-end encryption where feasible (especially chat/call metadata separation).
- Audit logs for account and privacy actions.

## 6) Reliability
- Use queue-based notification retries.
- Timeout and fallback from video call to chat/voice.
- Regional storage + CDN for low-latency media delivery.

## 7) Deployment
- Dockerized services.
- Managed Postgres + Redis.
- CI/CD pipeline with staging + production.
- IaC using Terraform for repeatable infrastructure.
