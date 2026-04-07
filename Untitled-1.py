#!/usr/bin/env python3
# Advanced Hand Gestures - Python Version

import asyncio
from mistyPy import MistyPy
from mistyPy.Robot import ArmPosition

class AdvancedHandGestures:
    def __init__(self):
        self.misty = MistyPy("YOUR_ROBOT_IP")  # Replace with robot IP
    
    async def initialize(self):
        await self.misty.power_system_led(0)
        await self.misty.speak("Advanced gestures ready")
        print("Advanced Hand Gestures Ready!")
        
        # Register all buttons
        await self.misty.register_single_button_event("Btn0", 0, self.button_handler)
        await self.misty.register_single_button_event("Btn1", 1, self.button_handler)
        await self.misty.register_single_button_event("Btn2", 2, self.button_handler)
        await self.misty.register_single_button_event("Btn3", 3, self.button_handler)
    
    async def button_handler(self, event):
        button_id = event['message'].get('buttonName', '')
        print(f"Button {button_id} pressed")
        
        if button_id == "0":
            await self.right_hand_wave()
        elif button_id == "1":
            await self.left_hand_point()
        elif button_id == "2":
            await self.both_hands_clap()
        elif button_id == "3":
            await self.right_hand_up()
        else:
            await self.stop_all()
    
    async def right_hand_wave(self):
        """Wave with right hand"""
        await self.misty.speak("Right hand wave")
        for i in range(3):
            await self.misty.move_arm(ArmPosition.RIGHT_ARM, 20, 30)
            await asyncio.sleep(0.3)
            await self.misty.move_arm(ArmPosition.RIGHT_ARM, -20, 30)
            await asyncio.sleep(0.3)
        await self.misty.move_arm(ArmPosition.RIGHT_ARM, 0, 50)
    
    async def left_hand_point(self):
        """Point with left hand"""
        await self.misty.speak("Left hand pointing")
        await self.misty.move_arm(ArmPosition.LEFT_ARM, 40, 40)
        await asyncio.sleep(1.5)
        await self.misty.move_arm(ArmPosition.LEFT_ARM, 0, 50)
    
    async def both_hands_clap(self):
        """Clap hands"""
        await self.misty.speak("Clapping")
        await self.misty.move_arm(ArmPosition.RIGHT_ARM, 25, 60)
        await self.misty.move_arm(ArmPosition.LEFT_ARM, 25, 60)
        await asyncio.sleep(0.5)
        await self.misty.move_arm(ArmPosition.RIGHT_ARM, 0, 60)
        await self.misty.move_arm(ArmPosition.LEFT_ARM, 0, 60)
        await asyncio.sleep(0.3)
        await self.misty.move_arm(ArmPosition.RIGHT_ARM, 25, 60)
        await self.misty.move_arm(ArmPosition.LEFT_ARM, 25, 60)
        await asyncio.sleep(0.5)
        await self.misty.move_arm(ArmPosition.RIGHT_ARM, 0, 60)
        await self.misty.move_arm(ArmPosition.LEFT_ARM, 0, 60)
    
    async def right_hand_up(self):
        """Raise right hand"""
        await self.misty.speak("Right hand up")
        await self.misty.move_arm(ArmPosition.RIGHT_ARM, 90, 40)
        await asyncio.sleep(2.0)
        await self.misty.move_arm(ArmPosition.RIGHT_ARM, 0, 50)
    
    async def stop_all(self):
        await self.misty.speak("Stopping")
        await self.misty.move_arm(ArmPosition.RIGHT_ARM, 0, 100)
        await self.misty.move_arm(ArmPosition.LEFT_ARM, 0, 100)
        await self.misty.move_head_position(0, 0, 0)

async def main():
    gestures = AdvancedHandGestures()
    await gestures.initialize()
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
    