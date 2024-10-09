import sys
import time
import asyncio
import random
sys.dont_write_bytecode = True
from random import randint
from hokireceh_claimer import base
from core.info import get_info
from core.task import process_do_task, process_boost_speed
from core.mint import process_mint_worm
from core.game import process_break_egg
from core.upgrade import process_upgrade

class Birds:
    def __init__(self):
        # Get file directory
        self.data_file = base.file_path(file_name="data.txt")
        self.config_file = base.file_path(file_name="config.json")

        # Initialize line
        self.line = base.create_line(length=50)

        # Initialize banner
        self.banner = base.create_banner(game_name="Birds")

        # Get config
        self.auto_do_task = base.get_config(
            config_file=self.config_file, config_name="auto-do-task"
        )

        self.auto_boost_speed = base.get_config(
            config_file=self.config_file, config_name="auto-boost-speed"
        )

        self.auto_mint_worm = base.get_config(
            config_file=self.config_file, config_name="auto-mint-worm"
        )

        self.auto_break_egg = base.get_config(
            config_file=self.config_file, config_name="auto-break-egg"
        )

        self.auto_upgrade_egg = base.get_config(
            config_file=self.config_file, config_name="auto-upgrade-egg"
        )

    async def main(self):  # Make the main function async
        while True:
            base.clear_terminal()
            print(self.banner)
            data = open(self.data_file, "r").read().splitlines()
            num_acc = len(data)
            base.log(self.line)
            base.log(f"{base.green}Number of accounts: {base.white}{num_acc}")

            for no, data in enumerate(data):
                base.log(self.line)
                base.log(f"{base.green}Account number: {base.white}{no+1}/{num_acc}")

                try:
                    get_info(data=data)

                    # Do task
                    if self.auto_do_task:
                        base.log(f"{base.yellow}Auto Do Task: {base.green}ON")
                        process_do_task(data=data)
                        wait_time = random.uniform(5, 10)
                        base.log(f"{base.yellow}Waiting for {wait_time:.2f} seconds before next task...")
                        await asyncio.sleep(wait_time)
                    else:
                        base.log(f"{base.yellow}Auto Do Task: {base.red}OFF")

                    # Boost speed
                    if self.auto_boost_speed:
                        base.log(f"{base.yellow}Auto Boost Speed: {base.green}ON")
                        process_boost_speed(data=data)
                        wait_time = random.uniform(5, 10)
                        base.log(f"{base.yellow}Waiting for {wait_time:.2f} seconds before next task...")
                        await asyncio.sleep(wait_time)
                        
                    else:
                        base.log(f"{base.yellow}Auto Boost Speed: {base.red}OFF")

                    # Mint worm
                    if self.auto_mint_worm:
                        base.log(f"{base.yellow}Auto Mint Worm: {base.green}ON")
                        process_mint_worm(data=data)
                        wait_time = random.uniform(5, 10)
                        base.log(f"{base.yellow}Waiting for {wait_time:.2f} seconds before next task...")
                        await asyncio.sleep(wait_time)
                    else:
                        base.log(f"{base.yellow}Auto Mint Worm: {base.red}OFF")

                    # Break egg
                    if self.auto_break_egg:
                        base.log(f"{base.yellow}Auto Break Egg: {base.green}ON")
                        process_break_egg(data=data)
                        wait_time = random.uniform(5, 10)
                        base.log(f"{base.yellow}Waiting for {wait_time:.2f} seconds before next task...")
                        await asyncio.sleep(wait_time)
                    else:
                        base.log(f"{base.yellow}Auto Break Egg: {base.red}OFF")

                    # Upgrade egg
                    if self.auto_upgrade_egg:
                        base.log(f"{base.yellow}Auto Upgrade Egg: {base.green}ON")
                        process_upgrade(data=data)
                        wait_time = random.uniform(5, 10)
                        base.log(f"{base.yellow}Waiting for {wait_time:.2f} seconds before next task...")
                        await asyncio.sleep(wait_time)
                    else:
                        base.log(f"{base.yellow}Auto Upgrade Egg: {base.red}OFF")

                    get_info(data=data)

                except Exception as e:
                    base.log(f"{base.red}Error: {base.white}{e}")

            print()
            wait_time = randint(3600, 7200)
            base.log(f"{base.yellow}Wait for {int(wait_time/60)} minutes!")
            await asyncio.sleep(wait_time) 

if __name__ == "__main__":
    try:
        birds = Birds()
        asyncio.run(birds.main()) 
    except KeyboardInterrupt:
        sys.exit()
