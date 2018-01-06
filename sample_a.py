def get_w4_start_date(days):
    '''Start date formatted for w4 network'''
    return (date.today() - timedelta(days=days)).strftime('%m/%d/%Y')


def get_w4_end_date():
    '''End date formatted for w4 network'''
    return (date.today() + timedelta(days=1)).strftime('%m/%d/%Y')


def get_w4_conversions(data, days):
    '''Fetch conversion data from the w4 network'''

    params = {
        'api_url': data['api_url'],
        'api_key': data['api_key'],
        'affiliate_id': data['affiliate_id'],
        'start_date': get_w4_start_date(days),
        'end_date': get_w4_end_date(),
        'limit': 500,
        'count': 'true'
    }

    api_url = ( '{api_url}' +
                '?key_id={api_key}' +
                '&min_date={start_date}' +
                '&max_date={end_date}' +
                '&limit={limit}' +
                '&count={count}').format(**params)


    r = requests.get(api_url)
    r = r.json()

    conversion_data = r['conversions']
    conversions = []

    for con in conversion_data:
        conversions.append({
            'conversion_id': con['conversion_id'],
            'created_ts': con['date_time'],
            'offer_id': con['offer_id']],
            'subid': con['sub_id'],
            'send_token': con['sub_id_2'],
            'revenue': con['payout']
        })

    return conversions
