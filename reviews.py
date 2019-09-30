#!/usr/bin/env python
#coding:utf-8
import requests
import time

user_ids_dict = {}
request_num = {}
reviews_numbers = []


#['25', '2', '246', '4114', '393', '2151', '4452', '4022', '472', '366']
def reviewsnum():
    user_ids = [24993, 26210, 18405, 10819, 16126, 12865, 8199, 10814, 6716, 12748]
    reviews_number_url = 'http://m.8673h.com/Action/ServiceInfo.do'
    for user_id in user_ids:
        reviews_number = eval(requests.post(reviews_number_url, {"service_id": str(user_id)}).text)
        reviews_number = reviews_number['data']['review'][0]['reviews_number']
        reviews_numbers.append(reviews_number)
        re_num = int(reviews_number) // 100 + 1
        request_num[user_id] = re_num
        user_ids_dict[user_id] = reviews_number
        # print('reviews_number:%s' % reviews_number)

    print(user_ids_dict)
    print(reviews_numbers)
    print(request_num)


def getreviews():
    request_num = {24993: 1, 26210: 1, 18405: 3, 10819: 42, 16126: 4, 12865: 22, 8199: 45, 10814: 41, 6716: 5, 12748: 4}
    # request_num = {18405: 3}
    reviews_url = 'http://m.8673h.com/Action/ServiceReviewsList.do'
    detail_reviews = {}
    num = 0
    print('start at %s' % time.ctime())
    for service_id, num in request_num.items():
        review_list = []
        for i in range(1, num + 1):
            data = {'service_id': service_id, 'nowPage': i, 'pageSize': 100}
            reviews_list = eval(requests.post(reviews_url, data).text)['data']
            for review in reviews_list:
                review_list.append(review['detail_reviews'])
            num=num+review_list.__len__()
            detail_reviews[str(service_id)] = review_list
            # time.sleep(0.6)
    print('end at %s' % time.ctime())
    print(detail_reviews)
    print('num:%s' % str(num))

    with open('reviews.txt', 'w') as r:
        r.write(str(detail_reviews))


if __name__ == '__main__':
    getreviews()
