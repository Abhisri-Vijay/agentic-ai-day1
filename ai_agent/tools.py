from data.course_fees import COURSE_FEES
import ast
import operator

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}


def get_course_fee(course_code):
    course_code = course_code.upper()
    return COURSE_FEES.get(course_code)


def safe_calculate(node):
    if isinstance(node, ast.Expression):
        return safe_calculate(node.body)

    if isinstance(node, ast.Constant):
        return node.value

    if isinstance(node, ast.BinOp):
        left = safe_calculate(node.left)
        right = safe_calculate(node.right)
        return OPERATORS[type(node.op)](left, right)

    raise ValueError("Unsupported expression")


def calculate(expression):
    tree = ast.parse(expression, mode="eval")
    return safe_calculate(tree)