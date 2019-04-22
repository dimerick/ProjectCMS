from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from .models import SliderActive, Slide, Partner, TeamMember, Activity

@plugin_pool.register_plugin
class MainSliderPlugin(CMSPluginBase):
	model = SliderActive
	name = ("Slider Plugin")
	render_template = "slider.html"
	cache = False

	def render(self, context, instance, placeholder):
		context['instance'] = instance
		context['id_slider'] = instance.slider_id
		context['slides'] = Slide.objects.filter(slider__id=instance.slider_id, is_active=True).order_by('position')
		return context


@plugin_pool.register_plugin
class PartnerPlugin(CMSPluginBase):
	model = CMSPlugin
	name = ("Partners Plugin")
	render_template = "partner_list.html"
	cache = False

	def render(self, context, instance, placeholder):
		context['instance'] = instance
		context['partners'] = Partner.objects.filter(is_active=True).order_by('position')
		#context['num_partners'] = len(context['partners'])
		return context


@plugin_pool.register_plugin
class TeamMemberPlugin(CMSPluginBase):
	model = CMSPlugin
	name = ("Team Members Plugin")
	render_template = "member_list.html"
	cache = False

	def render(self, context, instance, placeholder):
		context['instance'] = instance
		tmp_members = TeamMember.objects.filter(is_active=True).order_by('position')
		members = []
		i = 1
		for member in tmp_members:
			m = {'name':member.name, 'rol':member.rol, 'email':member.email, 'description':member.description, 
			'url_profile':member.url_profile, 'is_active':member.is_active, 'position':member.position, 
			'image':member.image, 'side':i%2}

			# m = {'name':member['name'], 'rol':member['rol'], 'email':member['email'], 'description':member['description'], 
			# 'url_profile':member['url_profile'], 'is_active':member['is_active'], 'position':member['position'], 
			# 'image':member['image'], 'side':i%2}


			i = i + 1
			members.append(m)
			
		context['members'] = members	
		#context['num_partners'] = len(context['partners'])
		return context

@plugin_pool.register_plugin
class ActivityPlugin(CMSPluginBase):
	model = CMSPlugin
	name = ("Activities Plugin")
	render_template = "activity_list.html"
	cache = False

	def render(self, context, instance, placeholder):
		context['instance'] = instance
		tmp_activities = Activity.objects.filter(is_active=True).order_by('-date')
		activities = []
		i = 1
		for act in tmp_activities:
			a = {'name':act.name, 'description':act.description, 
			'date':act.date, 'url': act.url, 'is_active':act.is_active, 'image':act.image, 'side':i%2}

			i = i + 1
			activities.append(a)
			
		context['activities'] = activities
		#context['num_partners'] = len(context['partners'])
		return context