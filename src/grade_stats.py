"""学生成绩统计工具 —— 岗位实践实验一练习项目。"""

from typing import Iterable, List, Dict


def average(scores: Iterable[float]) -> float:
    """返回平均分；空输入返回 0.0。"""
    values: List[float] = list(scores)
    if not values:
        return 0.0
    return sum(values) / len(values)


def highest(scores: Iterable[float]) -> float:
    """返回最高分；空输入返回 0.0。"""
    values = list(scores)
    return max(values) if values else 0.0


def lowest(scores: Iterable[float]) -> float:
    """返回最低分；空输入返回 0.0。"""
    values = list(scores)
    return min(values) if values else 0.0


def grade_of(score: float) -> str:
    """按分数返回等级。"""
    if score >= 90:
        return "优"
    if score >= 80:
        return "良"
    if score >= 70:
        return "中"
    if score >= 60:
        return "及格"
    return "不及格"


def grade_distribution(scores: Iterable[float]) -> Dict[str, int]:
    """统计各等级人数。"""
    result = {"优": 0, "良": 0, "中": 0, "及格": 0, "不及格": 0}
    for s in scores:
        result[grade_of(s)] += 1
    return result


def parse_scores(text: str) -> List[float]:
    """把 '88,92,75' 这样的字符串解析成分数列表，忽略空白项。"""
    scores: List[float] = []
    for part in text.replace("\n", ",").split(","):
        part = part.strip()
        if part:
            scores.append(float(part))
    return scores

def pass_rate(scores: Iterable[float], pass_line: float = 60) -> float:
    """返回及格率（0~1）；空输入返回 0.0。"""
    values = list(scores)
    if not values:
        return 0.0
    passed = sum(1 for s in values if s >= pass_line)
    return passed / len(values)

def to_csv(scores: Iterable[float]) -> str:
    """把成绩导出成 CSV 文本（表头 + 每行一个成绩）。"""
    lines = ["score"]
    lines += [str(s) for s in scores]
    return "\n".join(lines)

def summarize(scores: Iterable[float]) -> Dict[str, object]:
    """汇总统计结果。"""
    values = list(scores)
    return {
        "count": len(values),
        "average": round(average(values), 2),
        "highest": highest(values),
        "lowest": lowest(values),
        "distribution": grade_distribution(values),
    }


if __name__ == "__main__":
    demo = parse_scores("88,92,75,60,45,99")
    print("成绩：", demo)
    print("汇总：", summarize(demo))
