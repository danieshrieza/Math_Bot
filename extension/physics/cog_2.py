from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from config import guild_id
from nextcord.ext.commands.context import Context


# NOTE : Class for EnergyAndForce
class EnergyAndForce(commands.Cog) :


    # NOTE : Initialize parameter for class
    def __init__(self, bot : commands.Bot) :
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to calculate moment of force of an object 
    @ nextcord.slash_command(
        description = "Calculate the moment of force of an object."
    )

    async def moment_of_force(self, ctx : Interaction, force : float, perpendicular_distance : float) :

        exp = f"{force} N × {perpendicular_distance} m "
        evalu = force * perpendicular_distance

        embed_msg = nextcord.Embed(
            title = "Physics Query", 
            description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"``` {exp} ```", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu} N m`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate the pressure acts on an object 
    @ nextcord.slash_command(
        description = "Calculate the pressure acts on an object."
    )

    async def pressure(self, ctx : Interaction, force : float, surface_area : float) :

        exp = f"{force} N ÷ {surface_area} m²"
        evalu = force/surface_area

        embed_msg = nextcord.Embed(
            title = "Physics Query", 
            description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"``` {exp} ```", 
            inline = False
        )
        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu} N/m²`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)
    

    # NOTE : Command to calculate the density of an object 
    @ nextcord.slash_command(
        description = "Calculate the density of an object."
    )

    async def density(self, ctx : Interaction, mass : float, volume : float) :

        exp = f'{mass} g ÷ {volume} cm³'
        evalu = mass/volume

        embed_msg = nextcord.Embed(
            title = "Physics Query", 
            description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"``` {exp} ```", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu} g/cm³`", 
            inline = True
        )
        
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate the work done of an object 
    @ nextcord.slash_command(
        description = "Calculate the work done of an object."
    )

    async def work_done(self, ctx : Interaction, force : float, distance : float) :

        exp = f'{force} N × {distance} m'
        evalu = force * distance

        embed_msg = nextcord.Embed(
            title = "Physics Query", 
            description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"``` {exp} ```", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu} J`", 
            inline = True
        )
        
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate the power possessed by an object 
    @ nextcord.slash_command(
        description = "Calculate the power possessed by an object."
    )

    async def power(self, ctx : Interaction, force : float, distance : float, time : float) :

        exp = f'({force} N × {distance} m) ÷ {time} s'
        evalu = (force * distance) / time

        embed_msg = nextcord.Embed(
            title = "Physics Query", 
            description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"``` {exp} ```", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu} W`", 
            inline = True
        )
        
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate the gravitational potential energy possessed by an object 
    @ nextcord.slash_command(
        description = "Calculate the gravitational potential energy possessed by an object."
    )

    async def grav_potential_energy(self, ctx : Interaction, mass : float, distance : float) :

        exp = f'{mass} kg × 9.8 m/s × {distance} m'
        evalu = mass * 9.8 * distance

        embed_msg = nextcord.Embed(
            title = "Physics Query", 
            description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"``` {exp} ```", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu} J`", 
            inline = True
        )
        
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate the elastic potential energy possessed by an object 
    @ nextcord.slash_command(
        description = "Calculate the elastic potential energy possessed by an object."
    )

    async def elas_potential_energy(self, ctx : Interaction, force : float, original_length : float, new_length : float) :

        exp = f'1/2 × {force} N × ({original_length} - {new_length}) m'
        evalu = 1/2 * (force * (original_length - new_length))

        embed_msg = nextcord.Embed(
            title = "Physics Query", 
            description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"``` {exp} ```", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu} J`", 
            inline = True
        )
        
        embed_msg.set_thumbnail(url = self.link)


    # NOTE : Command to calculate the kinetic energy possessed by an object 
    @ nextcord.slash_command(
        description = "Calculate the kinetic energy possessed by an object."
    )

    async def kinetic_energy(self, ctx : Interaction, mass : float, distance : float, time : float) :

        exp = f'1/2 × {mass} kg × ({distance / time} m/s)²'
        evalu = 1/2 * mass * (distance / time) ** 2

        embed_msg = nextcord.Embed(
            title = "Physics Query", 
            description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"``` {exp} ```", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu} J`", 
            inline = True
        )
        
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


# NOTE : Add EnergyAndForce to the bot
def setup(bot : commands.Bot) :
    bot.add_cog(EnergyAndForce(bot))