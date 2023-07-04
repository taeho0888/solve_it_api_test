import requests

BASE_URL = "https://solved.ac/api/v3"


class HTTPError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code
        super().__init__(
            f"HTTP Error: received status code {self.status_code}")


def request_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPError(response.status_code)
    return response.json()


def get_solvedac_problems(user_id, page_num=1):
    solvedCount = request_url(
        f'{BASE_URL}/user/show?handle={user_id}').get("solvedCount")

    problem_list = list()

    for i in range(1, solvedCount//50 + 2):
        problem_items = request_url(
            f'{BASE_URL}/search/problem?query=@{user_id}&page={i}').get('items')

        for item in problem_items:
            problem_list.append(item['problemId'])

    return problem_list


# user_id = 'shiftpsh'
user_id = input('백준 아이디를 입력해주세요: ')
problem_id_list = get_solvedac_problems(user_id)

if problem_id_list is not None:
    print(problem_id_list)
    print('푼 문제 수:', len(problem_id_list))
