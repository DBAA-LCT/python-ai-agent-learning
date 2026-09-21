






def get_passed_num(scores: list[int]) -> int:
    passed_count = sum(score >= 60 for scores in scores)
    return passed_count
