import math

def compute_quadratic_roots(a, b, c):
    if a == 0:
        raise ValueError("Hệ số 'a' không được bằng 0.")
    
    delta = b**2 - 4*a*c
    
    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        return (root1, root2)
    elif delta == 0:
        root = -b / (2*a)
        return (root, root)
    else:
        raise ValueError("Phương trình vô nghiệm (nghiệm phức).")