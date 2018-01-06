def get_non_momentum_route_data(cursor, route_id):
    '''
    Return data necessary to send non-momentum accounts using 3po, including:
    service, service_type, proxy, send_api_type, and send_api_auth.
    '''

    non_momentum_route_sql = '''
        SELECT
            service,
            service_type,
            proxy
        FROM trigger_scratch.non_momentum_routes
        WHERE route_id = {0}
    '''

    non_momentum_route_data = {}
    cursor.execute(non_momentum_route_sql.format(route_id))

    for (service, service_type, proxy) in cursor.fetchall():
        _, pwd = cogomail.get_misc_account(cursor, service)

        non_momentum_route_data['service'] = service
        non_momentum_route_data['service_type'] = service_type
        non_momentum_route_data['proxy'] = proxy
        non_momentum_route_data['send_api_type'] = service_type
        non_momentum_route_data['send_api_pwd'] = pwd

    return non_momentum_route_data
