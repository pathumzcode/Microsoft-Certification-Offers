# Contributing

Thank you for helping keep this independent guide accurate and useful. The official LevelUp terms and Microsoft exam-provider instructions take precedence over community documentation.

## Report outdated programme rules

1. Check the current [official voucher terms](https://skillupwithlevelup.com/cert-terms-and-conditions), [LevelUp FAQ](https://skillupwithlevelup.com/faqs), or other relevant official source.
2. Open a [documentation correction issue](.github/ISSUE_TEMPLATE/documentation-correction.md).
3. Name the affected file or section, quote or summarize what the official source now says, include its URL, and include the date you checked it.
4. Do not include passwords, personal email addresses, account identifiers, private learner data, or voucher codes.

If the source is unavailable or ambiguous, report the fact as unclear or needing manual verification rather than guessing.

## Submit a correction

- Make focused changes and use clear, beginner-friendly English.
- Keep offer-specific rules clearly labelled as offer-specific. Do not convert a condition into a promise.
- Cite official sources adjacent to claims that can change. Record the verification date in `docs/10-official-resources.md`.
- Preserve existing user content and do not add claims about eligibility, exam benefits, or interface controls unless an official source supports them.

## Screenshots

- Add screenshots only from public pages or accounts you are authorized to use.
- Never fabricate a screen, result, voucher, email, or badge.
- Use the numbered names and capture instructions in [screenshots/README.md](screenshots/README.md) and update [screenshots/manifest.md](screenshots/manifest.md).
- Place each screenshot or pending TODO immediately after its step's instructions, followed by a concise italic caption and an expected-result sentence. Avoid literal “Description:” or “Action:” labels.
- Record your chosen public display name or handle for screenshot credit, or **Anonymous** if you prefer. Obtain consent before publishing identifying attribution; never infer credit for an existing image.
- Attribution is a credit record, not a licence grant. Contribute only screenshots you are authorized to share.
- Redact names, emails, account identifiers, personal data, and voucher codes. Never commit a live code, password, or other secret.
- Include concise, accurate alt text and do not use an image to imply endorsement.

## Accessible Markdown

- Use descriptive headings in a logical order.
- Write meaningful link text and image alt text.
- Prefer short paragraphs and define acronyms on first use.
- Use tables only for compact structured data; make headings descriptive.
- Do not rely on color, layout, or screenshots alone to communicate a requirement.

## Test and submit a pull request

Run the documentation validator from the repository root:

```powershell
python scripts\validate_docs.py
```

Check that local Markdown links and images work, screenshots are listed in the manifest, and the README's status and verification date remain accurate. Then submit a pull request describing the change, the official sources consulted, and any facts that remain uncertain. The automated workflow also runs the validator on pushes and pull requests.
