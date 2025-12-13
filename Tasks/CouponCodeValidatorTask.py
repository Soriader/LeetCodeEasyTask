def validateCoupons(self, code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
    order = {
        "electronics": 0,
        "grocery": 1,
        "pharmacy": 2,
        "restaurant": 3,
    }

    def is_valid_code(s: str) -> bool:
        return bool(s) and all(ch.isalnum() or ch == '_' for ch in s)

    filtered = []

    for c, bl, active in zip(code, businessLine, isActive):
        bl_norm = bl.lower()
        if active and bl_norm in order and is_valid_code(c):
            filtered.append((order[bl_norm], c))

    filtered.sort(key=lambda x: (x[0], x[1]))

    return [c for _, c in filtered]

#https://leetcode.com/problems/coupon-code-validator/description/?envType=daily-question&envId=2025-12-13