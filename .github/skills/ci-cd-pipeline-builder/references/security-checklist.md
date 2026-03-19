# Security Checklist

- Pin third-party actions to immutable SHAs where feasible
- Use the minimum required `permissions`
- Never print secrets or derived credentials
- Validate untrusted input before shell use
- Restrict scheduled workflows to trusted branches
- Prefer OIDC over long-lived cloud credentials
- Add `timeout-minutes` to every job
