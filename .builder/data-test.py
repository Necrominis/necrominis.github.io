from weakref import weakref # Prevents memory leaks when deleting objects with circular references/dependencies.
from datetime import datetime # datetime(YYY, MM, DD)


	# ============================================================================ #
	#                                   CLASSES                                    #
	# ============================================================================ #


class Data:
	website_url: str = ""
	tags: '[Tag]' = []
	manufacturers: '[Manufacturer]' = []
	paints: '[PaintBrand]' = []
	supplies: '[SupplyCategory]' = []
	pages: '[Page]' = []


class Tag:
	def __init__(self, id: str, text: str, color: str, linked_page: 'Page'):
		self.id = id
		self.text = text
		self.color = color
		self.linked_page = weakref(linked_page)


class Manufacturer:
	def __init__(self, id: str, text: str, color: str, url: str):
		self.id = id
		self.text = text
		self.color = color


class PaintBrand:
	def __init__(self, id: str, text: str):
		self.id = id
		self.text = text
		self.lines: '[PaintLine]' = []


class PaintLine:
	def __init__(self, id: str, text: str, brand: 'PaintBrand'):
		self.id = id
		self.text = text
		self.brand = weakref(brand)
		self.colors: '[PaintColor]' = []

		if not self in brand.lines:
			brand.lines.append(weakref(self))


class PaintColor:
	def __init__(self, id: str, text: str, icon: str, official_name: str, url: str, line: 'PaintLine'):
		self.id = id
		self.text = text
		self.icon = icon
		self.official_name = official_name,
		self.url = url
		self.line = weakref(line)

		if not self in line.colors:
			line.colors.append(weakref(self))


class SupplyCategory:
	def __init__(self, id: str, text: str):
		self.id = id
		self.text = text
		self.brands: '[SupplyBrand]' = []


class SupplyBrand:
	def __init__(self, id: str, text: str, category: 'SupplyCategory'):
		self.id = id
		self.text = text
		self.items: '[SupplyItem]' = []
		self.category = weakref(category)

		if not self in category.brands:
			category.brands.append(weakref(self))


class SupplyItem:
	def __init__(self, id: str, text: str, icon: str, official_name: str, url: str, brand: 'SupplyBrand'):
		self.id = id
		self.text = text
		self.icon = icon
		self.official_name = official_name
		self.url = url
		self.brand = weakref(brand)

		if not self in brand.items:
			brand.items.append(weakref(self))


class Page:
	def __init__(self, id: str, title: str, path: str):
		self.id = id
		self.title = title
		self.path = path


# Singleton.
class HomePage:
	def __init__(self):
		super().__init__("home", "Necrominis Painting Studio", "")


# Singleton.
class MyPaintsPage:
	def __init__(self):
		super().__init__("my-paints", "My Paints", "paints/")


# Singleton.
class MySuppliesPage:
	def __init__(self):
		super().__init__("my-supplies", "My Supplies", "supplies/")


# Singleton.
class GalleryPage:
	def __init__(self, tags: '[Tag]', pages: '[Page]'):
		super().__init__("gallery", "Gallery", "gallery/")
		self.tags: '[Tag]' = []
		self.pages: '[Page]' = []

		for tag in tags:
			self.tags.append(weakref(tag))
		for page in pages:
			self.pages.append(weakref(page))


class PostPropertiesModel:
	def __init__(self, text: str, url: str):
		self.text = text
		self.url = url


class PostProperties:
	def __init__(self, date_created: datetime, tags: '[Tag]', manufacturers: '[Manufacturer]', models: '[PostPropertiesModel]'):
		self.date_created = date_created
		self.tags: '[Tag]' = []
		self.manufacturers: '[Manufacturer]' = []
		self.models: '[PostPropertiesModel]' = []

		for tag in tags:
			if not tag in self.tags:
				self.tags.append(weakref(tag))
		for manufacturer in manufacturers:
			if not manufacturer in self.manufacturers:
				self.manufacturers.append(weakref(manufacturer))
		for model in models:
			if not model in self.models:
				self.models.append(weakref(model))


class PostPage:
	def __init__(self, id: str, title: str, properties: 'PostProperties', images: '[str]', paragraphs: '[str]', paints_used = '[PaintColor]'):
		super().__init__(id, title, f"post/{id}/")
		self.properties = properties
		self.images: '[str]' = []
		self.paragraphs: '[str]' = []
		self.paints_used: '[PaintColor]' = []

		for image in images:
			images.append(image)
		for paragraph in paragraphs:
			paragraphs.append(paragraph)
		for paint in paints_used:
			self.paints_used.append(weakref(paint))


	# ============================================================================ #
	#                                     DATA                                     #
	# ============================================================================ #


class Data:
	website_url: str = ""
	tags: '[Tag]' = []
	manufacturers: '[Manufacturer]' = []
	paints: '[PaintBrand]' = []
	supplies: '[SupplyCategory]' = []
	pages: '[Page]' = []