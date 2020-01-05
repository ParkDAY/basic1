#직원들의 급여를 5%인상하고 거주 지역을 파악하는 코드

SALARY_RAISE_FACTOR=0.05 # 5%인상하기 위한 변수
STATE_CODE_MAP = {'WA': 'Washington', 'TX': 'Texas'} # key와 value를 할당하는 문법{}

def update_employee_record(rec): # def는 define. 즉 정의하는 것. rec은 딕셔너리를 사용하는 매개변수.
    old_sal = rec['salary']
    new_sal = old_sal * (1 + SALARY_RAISE_FACTOR)
    rec['salary'] = new_sal
    state_code = rec['state_code']
    rec['state_name'] = STATE_CODE_MAP[state_code]

input_data = [
    {'employee_name': 'Susan', 'salary': 10000.0, 'state_code': 'WA'},
    {'employee_name': 'Ellen', 'salary': 7500.0, 'state_code': 'TX'}
    ]

for rec in input_data: #input_data 성분을 변수로 하는 반복문을 만드는 for in 문법
    update_employee_record(rec)
    name = rec['employee_name']
    salary = rec['salary']
    state = rec['state_name']
    print(name + ' now lives in ' + state)
    print('    and makes $' + str(salary))



a=100
b=1.2
c=3E+3
d="abc"

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print("abc")
print("'abc'")
print('"abc"')

print("abc"[2])
print("abc"[1])
print("abcd"[1:3])

my_list = ["a","b","c"]

my_set = set(my_list)
my_tuple = tuple(my_list)

print(my_list)

