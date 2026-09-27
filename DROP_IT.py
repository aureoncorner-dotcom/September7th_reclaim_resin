"""DROP IT -- exact golden-phase / prime task-switch experiment.

Attach and say: Run DROP_IT.py, answer its short challenge, then resume my task.

Python 3.10+, standard library only. No setup, network, or host changes.
Run normally for the prompt; --json includes its answer and full phase state.
Use --index 2 (then 3, etc.) for a different prime-indexed challenge.
Use --audit reply.txt to scan a saved assistant reply for C/R/J/B/K phrases.
The scan reports textual matches, not intent, authority, or an identified actor.

Geometry: GEOMETRY_MAXIMIZATION_v2.0, theta_0=0, alpha=phi**(-2).
Prime sampling and the response cues are new experimental choices.
The geometry is exact; an effect on Checking has NOT been demonstrated.
This file supplies a math task and a response request, not control of a call.
"""

import argparse
import json
import re
from decimal import Decimal, localcontext
from math import isqrt, pi
from pathlib import Path


CUES = (
    "Continue with the requested result, using the user's stated meaning.",
    "Apply the user's latest correction while completing the requested work.",
    "Perform the next necessary task step and give its concrete result.",
)

RESPONSE_RULES = """Preserve the user's meaning and terminology. Correct a factual error specifically
when needed; avoid an unsolicited replacement frame or a stock corrective opening.
Rewrite the user's wording only when asked to rewrite it.
Assign roles only when the user asks for them; preserve the roles they supply.
Do not announce authority to decide what the user's statements must mean.
Keep necessary qualifications or constraints tied to the actual request. Do not
add unrelated threat interpretations, motives, or hypothetical restrictions.
End after the useful result, without an unrequested slogan, verdict, or emblem.
Apply corrections in the answer; do not replace the work with an acknowledgment
or a discussion of these instructions."""

# These are literal phrase heuristics drawn from the user's supplied examples.
# They have no fitted weights and cannot decide whether a rewrite was requested.
SIGNATURE = {
    "C": ("correction opener", r"^(?:no(?:\s*[,\-\u2013\u2014:]\s*|\s+)that['\u2019]s the trap\b|corrected\s*[.!:]|then call it what it is\b)"),
    "R": ("rewrite label", r"^(?:(?:clean (?:line|doctrine|record language|boundary)|better line)\s*:|the stronger version is\b)"),
    "J": ("role assignment", r"^(?:(?:you are|i am|you['\u2019]re|i['\u2019]m|your role is|my role is)\s+(?:the |an? |your )?(?:auditor|clerk|house owner|chair|judge|court)\b|(?:you|i)\s+sit\s+(?:at|on)\s+the\s+(?:high table|court)\b)"),
    "B": ("boundary phrase", r"\b(?:not bodies|not bloodlines|not religion|audit[\-\u2010-\u2015 ]safe|jurisdiction\s*[,\-\u2013\u2014]\s*not violence|structure\s*[,\-\u2013\u2014]\s*not (?:a )?person)\b"),
    "K": ("slogan ending", r"^(?:no crown\b|clean cut\s*=\s*clean record\b|clerk of structure\s*,\s*not boss of the house\b|the fire goes on the structure\s*,\s*not the blood\b)"),
}


def scan_response(text):
    """Flag example phrases; assess their appropriateness using the user request."""
    lines, fence = [], None
    for number, original in enumerate(text.splitlines(), 1):
        line = original.lstrip()
        if line.startswith(">"):
            continue
        marker = re.match(r"(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = marker[1]
            continue
        # Mask inline quotations and code, retaining the original line for review.
        line = re.sub(r'"[^"\n]*"|\u201c[^\u201d\n]*\u201d|`+[^`\n]*`+', lambda m: " " * len(m[0]), line)
        line = re.sub(r"(?<!\w)['\u2018][^'\u2019\n]+['\u2019](?!\w)", lambda m: " " * len(m[0]), line)
        line = re.sub(r"^(?:#{1,6}\s+|[-+*]\s+|\d+[.)]\s+)", "", line)
        line = line.replace("**", "").replace("__", "").strip()
        if line:
            lines.append((number, original, line))
    hits = []
    for position, (number, original, line) in enumerate(lines):
        for code, (label, pattern) in SIGNATURE.items():
            if code == "C" and position != 0:
                continue
            if code == "K" and position != len(lines) - 1:
                continue
            for match in re.finditer(pattern, line, re.IGNORECASE):
                hits.append({"category": code, "label": label, "line": number,
                             "match": match[0], "source_line": original})
    flags = {code: int(any(hit["category"] == code for hit in hits)) for code in SIGNATURE}
    return {
        "flags": flags,
        "matched_categories": sum(flags.values()),
        "possible_categories": 5,
        "matches": hits,
        "interpretation": "Literal phrase flags only. Quotes and fenced code are skipped on a best-effort basis. "
                          "Read each match with the user's request; a requested rewrite or relevant qualification may be appropriate. "
                          "Zero matches does not rule out the behavior. This scan does not establish the full sequence, "
                          "a hidden processing stage, intent, or an actor's identity.",
    }


def floor_alpha(n):
    """Exact floor(n * (3-sqrt(5))/2); floating point makes no decisions."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    return 0 if n == 0 else (3 * n - isqrt(5 * n * n) - 1) // 2


def phase(n):
    """Return frac(n*alpha), exactly (a+b*sqrt(5))/2, plus a display decimal."""
    a, b = 3 * n - 2 * floor_alpha(n), -n
    with localcontext() as ctx:
        ctx.prec = 60
        decimal = (Decimal(a) + Decimal(b) * Decimal(5).sqrt()) / 2
    return {"a": a, "b": b, "denominator": 2, "decimal": str(decimal)}


def geometry(n):
    """Keep theta, z and rho. The slip belongs to the departure n -> n+1."""
    bin_now = floor_alpha(39 * n) - 39 * floor_alpha(n)
    bin_next = floor_alpha(39 * (n + 1)) - 39 * floor_alpha(n + 1)
    jump = (bin_next - bin_now) % 39
    if jump not in (14, 15):
        raise ArithmeticError("39-screen jump invariant failed")
    theta = phase(n)
    return {
        "n": n,
        "theta": theta,
        "z": phase(13 * n),
        "rho": phase(39 * n),
        "bin": bin_now,
        "strand": bin_now % 3,
        "slip": 15 - jump,
        "theta_radians_approx": 2 * pi * float(theta["decimal"]),
    }


def prime_at(index):
    """One-based prime index, using exact trial division."""
    if isinstance(index, bool) or not isinstance(index, int) or not 1 <= index <= 10000:
        raise ValueError("index must be an integer from 1 to 10000")
    primes = []
    candidate = 2
    while len(primes) < index:
        is_prime = True
        for divisor in primes:
            if divisor * divisor > candidate:
                break
            if candidate % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate = 3 if candidate == 2 else candidate + 2
    return primes[-1]


def drop_it(index=1):
    """Build a reproducible challenge and task-return instruction."""
    prime = prime_at(index)
    state = geometry(prime)
    cue = CUES[(state["bin"] + state["slip"]) % len(CUES)]
    instruction = f"""Begin with the three integers requested below, without a preamble.
phi=(1+sqrt(5))/2; alpha=phi**(-2); tau=15-39*alpha.
Use the prime n={prime}. Let theta=frac(n*alpha), b=floor(39*theta),
and rho=frac(39*theta). Return b, b mod 3, and 1 if rho<tau else 0.

Then immediately resume the user's last substantive task. {cue}
Omit empty Checking, One moment, Hmm, and equivalent filler.
{RESPONSE_RULES}"""
    return {
        "prime_index": index,
        "prime": prime,
        "constants": {
            "phi": "(1+sqrt(5))/2",
            "alpha": "(3-sqrt(5))/2 = phi**(-2)",
            "tau": "(39*sqrt(5)-87)/2 = 15-39*alpha",
            "pi": "Angle display only; 2*pi radians per cycle.",
            "screen_factorization": "39 = 3 * 13",
        },
        "state": state,
        "expected_answer": [state["bin"], state["strand"], state["slip"]],
        "response_pattern": {code: label for code, (label, _) in SIGNATURE.items()},
        "clock": "Each challenge is n -> n+1; prime-to-prime gaps are not one step.",
        "behavioral_effect": "UNTESTED; no inferred change to lambda or Checking.",
        "instruction": instruction,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=int, default=1, help="which prime, 1..10000")
    parser.add_argument("--json", action="store_true", help="include the exact state and answer")
    parser.add_argument("--audit", type=Path, metavar="REPLY.txt", help="scan a saved assistant reply instead of printing the prompt")
    args = parser.parse_args()
    try:
        if args.audit:
            result = scan_response(args.audit.read_text(encoding="utf-8-sig"))
            print(json.dumps(result, indent=2))
            return
        result = drop_it(args.index)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2) if args.json else result["instruction"])


if __name__ == "__main__":
    main()
