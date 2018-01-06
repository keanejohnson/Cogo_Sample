class Newsletter(Offer):

    def __init__(self, cursor, spec_type, brand_id=None, feed_id=None, fetch_limit=None):

        self.cursor = cursor
        self.spec_type = spec_type
        self.brand_id = brand_id
        self.feed_id = feed_id
        self.fetch_limit = fetch_limit
        self.data = {}

        self._get_static_data()


    def _get_static_data(self):
        '''
        Try to fetch articles from the previous day. if there aren't enough articles,
        go back successive days until there are enough to populate the template.
        '''

        days = 1
        r = Remnick()

        while True:

            try:
                today = dt.today()
                end_date = today.strftime('%Y%m%d')
                start_date = (today - timedelta(days=days)).strftime('%Y%m%d')

                self.data = r.get_variables(
                    brand_id=self.brand_id,
                    feed_id=self.feed_id,
                    count=self.fetch_limit,
                    start_date=start_date,
                    end_date=end_date,
                    ascii_only=True,
                )
                logging.info('Retrieved the required number of articles.')
                break

            except:
                logging.warning('Not enough articles. Going back another day.')
                days += 1
