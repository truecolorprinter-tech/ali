# MVP Backlog (8-week practical plan)

## Phase 1 (Week 1-2): Foundation
- Define MVP requirements and acceptance criteria.
- Create database schema and auth flows.
- Build resident signup/login.
- Generate QR code and printable door card template.

## Phase 2 (Week 3-4): Visitor communication
- Build visitor landing page by QR slug.
- Implement real-time text chat.
- Implement voice recording/upload + playback.
- Add anti-spam challenge (rate limits, captcha if needed).

## Phase 3 (Week 5-6): Resident response app
- Build resident inbox and live conversation UI.
- Add push notifications for new visitors.
- Add availability states (online, busy, away).
- Add saved quick replies.

## Phase 4 (Week 7): Video + quality
- Add one-tap video call with WebRTC signaling.
- Fallback to text if call not answered.
- Add session quality metrics and call logs.

## Phase 5 (Week 8): Pilot release
- Add billing stub (free/pro tier toggle).
- Add analytics dashboard (response time, missed visits).
- Run pilot with first users and collect feedback.
- Prepare app store and web launch assets.

## Definition of done for MVP
- Visitor can scan and contact without signup.
- Resident receives and responds in under 5 seconds median.
- Voice messages are stored and playable.
- Basic abuse prevention + privacy policy in place.
