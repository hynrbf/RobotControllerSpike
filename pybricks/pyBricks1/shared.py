from pybricks.hubs import PrimeHub


class Shared:
    __hub = PrimeHub()

    @staticmethod
    def hub() -> PrimeHub:
        return Shared.__hub
