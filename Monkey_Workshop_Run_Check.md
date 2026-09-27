# Monkey Workshop — requested run check

Anonymous · CC0 · 2026-09-08

[Open the workshop](https://monkey-workshop-four.ronswansonbruv.chatgpt.site)

The executable checks passed again. The browser interaction check remains incomplete.

| Check | Result |
|---|---|
| Browser logic port against the original Python traces | 1,408 / 1,408 trials matched |
| Phase integration against the analytic solution | 1,202 checks passed; maximum error 3.73e-14 radians |
| String-model scaling and inverse pitch recovery | 81 checks passed |
| Live controls, rendering, and actual audio output | Not verified in this run |

The supervised browser preview required an additional development dependency. The installation attempt returned: “network approval was cancelled before a decision was returned.” No installed local copy was found for an offline fallback. The temporary preview configuration was removed; the published workshop source remains unchanged.

The browser skill permitted only the supported browser runtime, and the Sites preview instructions required the supervised preview address. No alternate browser-control or hosting path was used to bypass that boundary.

Validated source commit: `ec76877f6573c3d492c0a37b4c3520ddfd9d29c1`. The computational run used Node and did not interact with a browser. No new language-model trial, physical experiment, or speaker-output measurement was performed.

The preserved original benchmark separates 1,280 intact-checker trials (320 primary acceptances, 704 recoveries, 256 unresolved, zero wrong acceptances) from the separate 128 broken-checker trials (128 wrong acceptances).
