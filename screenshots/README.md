# Screenshot workflow

## Policy

Screenshots must be genuine captures of public pages or accounts the contributor is authorized to access. No fabricated account screens, scores, messages, voucher codes, or outcomes are allowed. For tutorial captures, use a desktop viewport (1366 × 768 or 1440 × 900), not a full-page capture. Add one transparent, bright-red rectangular outline about 3–5 px thick around the verified next action; keep the target readable and its surrounding context visible.

Never commit an active voucher code, password, verification code, candidate name, private email address, account identifier, booking reference, or other personal information. Redact these details before saving a file.

## Contributor attribution

For each new screenshot contribution, update `manifest.md` with the contributor's chosen public display name or handle, or record **Anonymous** if requested. Obtain the contributor's consent before publishing identifying attribution. Record the capture date and official source as well. Do not guess who created existing screenshots: their original attribution was not recorded in the repository. Attribution is a credit record only and does not grant reuse rights or select the repository's licence.

## Screenshot inventory

The [manifest](manifest.md) is the single source of truth for filenames, purposes, highlighted controls, guide references, capture status, and attribution. Captures document public pages at capture time; they do not establish that an offer remains available. Check the official terms for live status.

## Capture missing images on Windows

1. Open the relevant public page or an account you are authorized to use. Do not sign in for a screenshot in this community workflow unless you own/are authorized to use the account and can safely redact its contents.
2. Set the browser window to a desktop-sized viewport (1366 × 768 or 1440 × 900), at normal zoom. Do not use full-page capture.
3. Use Windows Snipping Tool: press **Win+Shift+S**, choose a rectangular capture, and select only the relevant browser area.
4. Add a transparent-interior bright-red rectangle, approximately 3–5 px thick, around the exact verified control. Keep one target per screenshot whenever possible; do not obscure its text.
5. Paste into an image editor that supports opaque redaction. Cover personal details and all voucher codes with solid blocks; cropping alone may leave sensitive information in the saved image.
6. Save as PNG using the numbered filename in [manifest.md](manifest.md).
7. Inspect the saved image at normal size to confirm the target, context, outline, and text are readable and redaction cannot be reversed. Remove metadata if it contains private information.
8. Add the screenshot immediately after the relevant step's instructions, followed by a concise italic caption and an expected-result sentence. Use meaningful alt text; do not add literal “Description:” or “Action:” labels.
9. Record the contributor's chosen display name or handle (or **Anonymous** by request), capture date, official source, purpose, and highlighted element in the manifest. Never infer credit for an existing image.
10. Change the manifest status from `Pending` to `Captured` only after inspecting the image and checking its target and alt text.
11. Run `python scripts\validate_docs.py`.

If you cannot safely create a real screenshot, leave it pending and explain why. Do not add an empty or mock image file.

## Planned screenshot checklist

See [manifest.md](manifest.md) for filenames, purposes, highlighted targets, guide references, capture instructions, contributor attribution, and status. Account verification, enrolment confirmation, learner progress, assessment, voucher email, profile details, and private booking screens remain pending unless safely supplied by an authorized contributor. Never fabricate an assessment result, voucher email, learner state, or booking confirmation.
