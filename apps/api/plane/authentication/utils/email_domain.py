# Copyright (c) 2023-present Plane Software, Inc. and contributors
# SPDX-License-Identifier: AGPL-3.0-only
# See the LICENSE file for details.

import os


def is_email_domain_allowed(email: str) -> bool:
    """
    Checks whether the email's domain is permitted by the org whitelist.

    Set ALLOWED_EMAIL_DOMAINS as a comma-separated list of domains, e.g.:
        ALLOWED_EMAIL_DOMAINS=acme.com,partner.org

    If ALLOWED_EMAIL_DOMAINS is not set or empty, all domains are allowed
    (backwards-compatible default — existing deployments are unaffected).
    """
    allowed_raw = os.environ.get("ALLOWED_EMAIL_DOMAINS", "").strip()
    if not allowed_raw:
        # No whitelist configured — permit every domain
        return True

    allowed_domains = {d.strip().lower() for d in allowed_raw.split(",") if d.strip()}
    if not allowed_domains:
        return True

    domain = email.split("@")[-1].lower()
    return domain in allowed_domains
