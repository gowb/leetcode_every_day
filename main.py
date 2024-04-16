import requests
from flask import Flask, render_template, request

app = Flask(__name__)
def getHtml(titleSlug):
    url2 = 'https://leetcode.cn/graphql/'

    headers2 = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': '_bl_uid=XglOeq9pgmacRb8jIny8dpnmh8j1; csrftoken=cJfhOApvqMzut7RxqwaA5LBA7Qff72iqS0uGJZkLZjk3B9Qoioqe7i6Cm73rwT3p; __appToken__=',
        'Origin': 'https://leetcode.cn',
        'Referer': 'https://leetcode.cn/problems/string-to-integer-atoi/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'authorization': '',
        'baggage': 'sentry-environment=production,sentry-release=97ebc0d1,sentry-transaction=%2Fproblems%2F%5Bslug%5D%2F%5B%5B...tab%5D%5D,sentry-public_key=1595090ae2f831f9e65978be5851f865,sentry-trace_id=9ae2128681bb42cd8d9a10ae1d53cf1b,sentry-sample_rate=0.03',
        'content-type': 'application/json',
        'random-uuid': 'f30bad04-a71c-2065-efb0-4f6e87f87cba',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sentry-trace': '9ae2128681bb42cd8d9a10ae1d53cf1b-b9db33a5aaa897c7-0',
        'x-csrftoken': 'cJfhOApvqMzut7RxqwaA5LBA7Qff72iqS0uGJZkLZjk3B9Qoioqe7i6Cm73rwT3p',
    }

    data2 = {
        "query": """
            query questionTranslations($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    translatedTitle
                    translatedContent
                }
            }
        """,
        "variables": {
            "titleSlug": titleSlug
        },
        "operationName": "questionTranslations"
    }

    response = requests.post(url2, json=data2, headers=headers2)
    response_json = response.json()
    # 提取 translatedTitle 和 translatedContent 字段
    translated_title = response_json["data"]["question"]["translatedTitle"]
    translated_content = response_json["data"]["question"]["translatedContent"]

    print("Translated Title:", translated_title)
    print("Translated Content:", translated_content)
    return translated_title, translated_content


def getQuestions(page):
    # 模拟从后端获取的数据

    url = 'https://leetcode.cn/graphql/'
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': '_bl_uid=XglOeq9pgmacRb8jIny8dpnmh8j1; csrftoken=cJfhOApvqMzut7RxqwaA5LBA7Qff72iqS0uGJZkLZjk3B9Qoioqe7i6Cm73rwT3p; __appToken__=',
        'Origin': 'https://leetcode.cn',
        'Referer': 'https://leetcode.cn/problemset/?page=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'authorization': '',
        'baggage': 'sentry-environment=production,sentry-release=97ebc0d1,sentry-transaction=%2Fproblemset%2F%5B%5B...slug%5D%5D,sentry-public_key=1595090ae2f831f9e65978be5851f865,sentry-trace_id=d7b7903de9ca4c17a41bd211fef2af7c,sentry-sample_rate=0.03',
        'content-type': 'application/json',
        'random-uuid': 'f30bad04-a71c-2065-efb0-4f6e87f87cba',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sentry-trace': 'd7b7903de9ca4c17a41bd211fef2af7c-98fdd1a5bee33c48-0',
        'x-csrftoken': 'cJfhOApvqMzut7RxqwaA5LBA7Qff72iqS0uGJZkLZjk3B9Qoioqe7i6Cm73rwT3p',
    }
    data = {
        "query": """
        query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
          problemsetQuestionList(
            categorySlug: $categorySlug
            limit: $limit
            skip: $skip
            filters: $filters
          ) {
            hasMore
            total
            questions {
              acRate
              difficulty
              freqBar
              frontendQuestionId
              isFavor
              paidOnly
              solutionNum
              status
              title
              titleCn
              titleSlug
              topicTags {
                name
                nameTranslated
                id
                slug
              }
              extra {
                hasVideoSolution
                topCompanyTags {
                  imgUrl
                  slug
                  numSubscribed
                }
              }
            }
          }
        }
      """,
        "variables": {
            "categorySlug": "all-code-essentials",
            "skip": int(page),
            "limit": 50,
            "filters": {}
        },
        "operationName": "problemsetQuestionList"
    }
    response = requests.post(url, json=data, headers=headers)
    # 获取问题列表
    questions = response.json()["data"]["problemsetQuestionList"]["questions"]

    # 提取所有titleSlug的值
    title_slugs = [question["titleSlug"] for question in questions]
    return title_slugs


@app.route('/')
def index():
    p = int(request.args.get('p', 0))
    q = int(request.args.get('q', 0))
    if p > 3397:
        p = 3397
    if q > 49:
        q = 49
    title_slugs = getQuestions(p)
    # print(title_slugs)
    translated_title, translated_content = getHtml(title_slugs[int(q)])
    return render_template('index.html', translated_title=translated_title, translated_content=translated_content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7700)
