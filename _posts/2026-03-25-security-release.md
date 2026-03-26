---
author: matmair
title: Action required - Upcoming Security Release
---

The InvenTree core development team has received a report of a *critical security vulnerability*  affecting a large range of releases since 2024. We will release a disclosure and a fixed release for the 1.2.x release series on 2026-04-08 21:00 UTC.  
The vulnerability allows for lateral movement and privilege escalation within an InvenTree instance. It has a low attack complexity.

## Steps to take now

We are not aware of active exploitation of this vulnerability, but we recommend that users take the following steps to mitigate risks:
- Do *not* expose your InvenTree instance to the public internet without hardening steps as laid out in the [threat model](https://docs.inventree.org/en/stable/concepts/threat_model/)
- Ensure *registration is disabled* till the release
- Ensure you *trust all users registered* on your instance, especially those with staff or higher permissions

The vulnerability has a low complexity and can be expected to be exploited once released. It is important to prepare to update or take your system off the public internet.

## Security Policy

As always with security related themes we remind all users, security researchers, and intrested parties of our [security policy](https://inventree.readthedocs.io/en/stable/security/).

If you have discovered a security vulnerability, please report it to us via the channels described in the policy. We take all reports seriously and will work to address any vulnerabilities in a timely manner.

We would like to thank the security researcher who reported this and several other vulnerabilities in a responsible manner, and we encourage others to do the same in the future. The reporter will be credited in the disclosure and CVE entry.
