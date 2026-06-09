# Security and Privacy

Muse is instruction-only, but the dreams it writes can be sensitive. Treat the
user's `dreams/` directory as private by default.

## Private data

Muse should not store:

- secrets, tokens, credentials, API keys, private keys, auth/session paths;
- raw private messages or sensitive communications;
- unredacted client details in public repos;
- health, money, career, or relationship details unless the user expects them in
  a private local workspace.

Prefer safe summaries and redacted pointers.

## Recommended `.gitignore`

In public or shared repos, users should add:

```gitignore
# Muse private dream data
dreams/
```

Only version `dreams/` intentionally, and only after reviewing its contents.

## External actions

Muse must not log in, submit forms, send messages, publish content, or mutate
external systems. External-facing outputs are draft-first and approval-gated.

## Scheduled runs

Cron/scheduled Muse runs are draft-only. They may write local dream files and
indexes, but they must not promote ideas or execute external actions.

## Reporting issues

If you find a privacy or security problem in the skill instructions, open a GitHub
issue without including real secrets or private user data. Use fake examples.
