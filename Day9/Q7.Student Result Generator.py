class Result:
    def calculate_result(self, sub1, sub2, sub3=None):
        if sub3 is not None:
            total = sub1 + sub2 + sub3
            print(f"Result (3 Subjects): {total}")
        else:
            total = sub1 + sub2
            print(f"Result (2 Subjects): {total}")
res = Result()
res.calculate_result(80, 90)
res.calculate_result(80, 90, 85)
