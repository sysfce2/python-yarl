from yarl import URL

MANY_HOSTS = [f"www.domain{i}.tld" for i in range(512)]
MANY_URLS = [f"https://www.domain{i}.tld" for i in range(512)]
BASE_URL = URL("http://www.domain.tld")
QUERY_URL = URL("http://www.domain.tld?query=1&query=2&query=3&query=4&query=5")
URL_WITH_PATH = URL("http://www.domain.tld/req")
QUERY_SEQ = {str(i): tuple(str(j) for j in range(10)) for i in range(10)}
SIMPLE_QUERY = {str(i): str(i) for i in range(10)}


def test_url_build_with_host_and_port(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            URL.build(host="www.domain.tld", path="/req", port=1234)


def test_url_build_encoded_with_host_and_port(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            URL.build(host="www.domain.tld", path="/req", port=1234, encoded=True)


def test_url_build_with_host(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            URL.build(host="domain")


def test_url_build_access_username_password(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            url = URL.build(host="www.domain.tld", user="user", password="password")
            url.raw_user
            url.raw_password


def test_url_build_access_raw_host(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            url = URL.build(host="www.domain.tld")
            url.raw_host


def test_url_build_access_fragment(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            url = URL.build(host="www.domain.tld")
            url.fragment


def test_url_build_access_raw_path(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            url = URL.build(host="www.domain.tld", path="/req")
            url.raw_path


def test_url_build_with_different_hosts(benchmark):
    @benchmark
    def _run():
        for host in MANY_HOSTS:
            URL.build(host=host)


def test_url_build_with_host_path_and_port(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            URL.build(host="www.domain.tld", port=1234)


def test_url_make_with_host_path_and_port(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            URL("http://www.domain.tld:1234/req")


def test_url_make_encoded_with_host_path_and_port(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            URL("http://www.domain.tld:1234/req", encoded=True)


def test_url_make_with_host_and_path(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            URL("http://www.domain.tld")


def test_url_make_with_many_hosts(benchmark):
    @benchmark
    def _run():
        for url in MANY_URLS:
            URL(url)


def test_url_make_access_raw_host(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            url = URL("http://www.domain.tld")
            url.raw_host


def test_url_make_access_fragment(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            url = URL("http://www.domain.tld")
            url.fragment


def test_url_make_access_raw_path(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            url = URL("http://www.domain.tld/req")
            url.raw_path


def test_url_make_access_username_password(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            url = URL("http://user:password@www.domain.tld")
            url.raw_user
            url.raw_password


def test_url_make_with_ipv4_address_path_and_port(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            URL("http://127.0.0.1:1234/req")


def test_url_make_with_ipv4_address_and_path(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            URL("http://127.0.0.1/req")


def test_url_make_with_ipv6_address_path_and_port(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            URL("http://[::1]:1234/req")


def test_url_make_with_ipv6_address_and_path(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            URL("http://[::1]/req")


def test_url_make_with_query_mapping(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            BASE_URL.with_query(SIMPLE_QUERY)


def test_url_make_with_query_sequence_mapping(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            BASE_URL.with_query(QUERY_SEQ)


def test_url_to_string(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            str(BASE_URL)


def test_url_with_path_to_string(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            str(URL_WITH_PATH)


def test_url_with_query_to_string(benchmark):
    @benchmark
    def _run():
        for _ in range(100):
            str(QUERY_URL)