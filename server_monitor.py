import psutil
import argparse


class ServerMonitor:

    @classmethod
    def get_cpu_usage(cls):
        cls._namedtuple_printer("cpu", psutil.cpu_times_percent(interval=0.0, percpu=False))

    @classmethod
    def get_mem_usage(cls):
        cls.get_virtual_mem_usage()
        cls.get_swap_mem_usage()

    @classmethod
    def get_virtual_mem_usage(cls):
        cls._namedtuple_printer("virtual", psutil.virtual_memory())

    @classmethod
    def get_swap_mem_usage(cls):
        cls._namedtuple_printer("swap", psutil.swap_memory())

    @classmethod
    def _namedtuple_printer(cls, prefix, data):
        for field in data._asdict():
            print("{prefix}.{field} {value}".format(prefix=prefix,
                                                    field=field,
                                                    value=data._asdict()[field]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Metrics usage params')
    parser.add_argument('usage_type', nargs='?', default=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.usage_type == "cpu":
        ServerMonitor.get_cpu_usage()
    elif args.usage_type == "mem":
        ServerMonitor.get_mem_usage()
