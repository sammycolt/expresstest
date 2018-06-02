def check(ans):
    try:
        ans = int(ans)
        return ans % 2 == 0
    except Exception:
        return False