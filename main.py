# from dataclasses import dataclass
from typing import Optional


# @dataclass
class Alignment:
    def __init__(self, opp):
        self.opp = opp
        # opp: float = 0


# @dataclass
class PaMa(Alignment):

    def pa_ve_ma(self):
        return (
                self.opp / 2
        )

    def pa_ho_ma(self):
        return (
                self.opp / 2
        )


# @dataclass
class AnMa(Alignment):
    def __init__(self, adj: float = 0, hub_dis: float = 0, rhdb=None):
        self.adj = adj
        self.hub_dis = hub_dis
        self.rhdb = rhdb

    hub_dis: float = 0
    rhdb: Optional = None

    def an_ve_ma(self) -> float:
        return (self.opp / self.adj) * self.hub_dis

    def an_ho_ma(self) -> float:
        return (self.opp / self.adj) * self.hub_dis


def main() -> None:
    select = input("Select alignment type: 1 for Angular and 2 for Parallel >>>    ")
    # while select <= 2:
    #     raise ValueError(f"You have to select 1 for Angular and 2 for Parallel")

    if select == 1:
        result = AnMa(adj=int(input('input your adj value')), hub_dis=int(input('hud_dis value')),
                      opp=int(input('opp value')))
        print(f'{result.an_ve_ma()} is your result')


    elif select == 2:
        result = PaMa(opp=int(input("Dial reading at the top of the hub?: ")))
        print(
            f'On the side where the dial is placed, push the motor inward to have {result.pa_ho_ma()} on the dial')

    else:
        raise ValueError(f"You have to select 1 for Angular and 2 for Parallel")


if __name__ == '__main__':
    main()
