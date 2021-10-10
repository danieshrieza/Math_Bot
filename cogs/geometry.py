import discord
from discord.ext import commands
from discord_slash import cog_ext

# ! <--- Class for Geometry_Calculation 
class Geometry_Calculation(commands.Cog) :

  # ? <--- Initialize variable for class
  def __init__(self, client):
    self.client = client
    self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/912c1601116f083c03ecc0a8a7b00697.png?size=128"

  # ? <--- Command to calculate circumference of a circle using radius
  @ cog_ext.cog_slash(description = "Calculate the circumference of a circle using radius.")
  async def rcircle_circumference(self,ctx,radius : float) :
    self.exp = f"2 × 22/7 × {radius}"
    self.eval = 2 * 22/7 * radius
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to calculate circumference of a circle using diameter
  @ cog_ext.cog_slash(description = "Calculate the circumference of a circle using diameter")
  async def dcircle_circumference(self,ctx, diameter : float) :
    self.exp = f"22/7 × {diameter}"
    self.eval = 22/7 * diameter
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Commmand to calculate area of a circle
  @ cog_ext.cog_slash(description = "Calculate the area of a circle.")
  async def area_circle(self,ctx,radius : float) :
    self.exp = f"22/7 × {radius}²"
    self.eval = 22/7 * radius ** 2
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to calculate area of a rectangle or a cube
  @ cog_ext.cog_slash(description = "Calculate the area of a rectangle or a square.")
  async def area_rectangle_square(self,ctx,length : float, width : float) :
    self.exp = f"{length} × {width}"
    self.eval = length * width
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to calculate area of a triangle
  @ cog_ext.cog_slash(description = "Calculate the area of a triangle.")
  async def area_triangle(self,ctx,base : float, height : float) :
    self.exp = f"1/2 × {base} × {height}"
    self.eval = 1/2 * base * height
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to calculate area of a parallelogram
  @ cog_ext.cog_slash(description = "Calculate the area of a parallelogram.")
  async def area_parallelogram(self,ctx,base : float, height : float) :
    self.exp = f"{base} × {height}"
    self.eval = base * height
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to calculate area of a kite
  @ cog_ext.cog_slash(description = "Calculate the area of a kite.")
  async def area_kite(self,ctx,long_diagonal : float, short_diagonal : float) :
    self.exp = f"1/2 × {long_diagonal} × {short_diagonal}"
    self.eval = 1/2 * long_diagonal * short_diagonal
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to calculate area of a trampezium
  @ cog_ext.cog_slash(description = "Calculate the area of a trampezium.")
  async def a_trampezium(self,ctx,first_parallel : float, second_parallel : float, height : float) :
    self.exp = f"1/2 × ({first_parallel + second_parallel}) × {height}"
    self.eval = 1/2 * (first_parallel + second_parallel) * height
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to calculate surface area of a cube
  @ cog_ext.cog_slash(description = "Calculate the surface area of a cube.")
  async def surface_area_cube(self,ctx,length : float) :
    self.exp = f"6 × {length}²"
    self.eval = 6 * (length ** 2)
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
  
  # ? <--- Command to calculate surface area of a cuboid
  @ cog_ext.cog_slash(description = "Calculate the surface area of a cuboid.")
  async def surface_area_cuboid(self,ctx,length : float, width : float, height : float) :
    self.exp = f"2({length} * {width}) + 2({length} × {height}) + 2({width} × {height})"
    self.eval = 2 * (length * width) + 2 * (length * height) + 2 * (width * height)
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  # ? <--- Command to calculate surface area of pyramid 
  @ cog_ext.cog_slash(description = "Calculate the surface area of a pyramid.")
  async def surface_area_pyramid(self,ctx,length : float, width : float, face_height : float) :
    self.exp = f"2(1/2 × {face_height} × {length/2}) + 2(1/2 × {face_height} × {width/2}) + ({length} × {width})"
    self.eval = 2 * (1/2 * face_height * (length/2)) + 2 * (1/2 * face_height *(width/2)) + (length * width)
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
  
  # ? <--- Command to calculate surface area of a cylinder
  @ cog_ext.cog_slash(description = "Calculate the surface area of a cylinder.")
  async def surface_area_cylinder(self,ctx,radius : float, height : float) :
    self.exp = f"(2 × 22/7 × {radius}²) + (2 × 22/7 × {radius} × {height})"
    self.eval = (2 * 22/7 * (radius ** 2)) + (2 * 22/7 * radius * height)
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  # ? <--- Command to calculate surface area of a cone
  @ cog_ext.cog_slash(description = "Calculate the surface area of a cone.")
  async def surface_area_cone(self,ctx,radius : float, slant_height : float) :
    self.exp = f"(22/7 × {radius}²) + (22/7 × {radius} × {slant_height})"
    self.eval = (22/7 * (radius ** 2)) + (22/7 * radius * slant_height)
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  # ? <--- Command to calculte surface area of a sphere
  @ cog_ext.cog_slash(description = "Calculate the surface area of a sphere.")
  async def surface_area_sphere(self,ctx,radius : float) :
    self.exp = f"4 × 22/7 × {radius}²"
    self.eval = 4 * 22/7 * (radius ** 2)
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to calculate volume of a cube or a cuboid
  @ cog_ext.cog_slash(description = "Calculate the volume of a cube or a cuboid.")
  async def volume_cube_cuboid(self,ctx,length : float, width : float, height : float) :
    self.exp = f"{length} × {width} × {height}"
    self.eval = length * width * height 
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to calculate volume of a pyramid
  @ cog_ext.cog_slash(description = "Calculate the volume of a pyramid.")
  async def volume_pyramid(self,ctx,length : float,width : float,height : float) :
    self.exp = f"1/3 × {length} × {width} × {height}"
    self.eval = 1/3 * length * width * height
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to calculate volume of a cylinder
  @ cog_ext.cog_slash(description = "Calculate the volume of a cylinder.")
  async def volume_cylinder(self,ctx,radius : float, height : float) :
    self.exp = f"22/7 × {radius}² × {height} "
    self.eval = 22/7 * (radius ** 2) * height
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  # ? <--- Command to calculate volume of a cone
  @ cog_ext.cog_slash(description = "Calculate the volume of a cone.")
  async def volume_cone(self,ctx,radius : float, height : float) :
    self.exp = f"1/3 × 22/7 × {radius}² × {height}"
    self.eval = 1/3 * 22/7 * (radius ** 2) * height
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to calculate volume of a sphere
  @ cog_ext.cog_slash(description = "Calculate the volume of a sphere.")
  async def volume_sphere(self,ctx,radius : float) :
    self.exp = f"4/3 × 22/7 × {radius}²"
    self.eval = 4/3 * 22/7 * (radius ** 2)
    self.user = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

# ! <--- Add Geometry_Calculation into the bot
def setup(client):
  client.add_cog(Geometry_Calculation(client))