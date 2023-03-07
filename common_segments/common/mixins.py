from tarot_cards.models import TarotSuits, Card


class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class TarotSetUpTestMixin:
    def setUp(self):
        self.suit = TarotSuits.objects.create(
            suits_name='test_suit',
            description='test_description',
            image_2='static/images/tarot_img/cups/2_cups.png',
            image_3='static/images/tarot_img/cups/3_cups.png',
            image_4='static/images/tarot_img/cups/2_cups.png',
            url='test-suit'
        )


class TarotMixin:
    """Mixin with shared methods for tarot views"""
    model = Card

    def get_object(self, queryset=None):
        """Sort the objects randomly and take the first object"""
        return self.get_queryset().order_by('?').first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.object.name
        context['image'] = self.object.image_1
        context['seo_description'] = self.object.seo_description
        context['seo_key_words'] = self.object.seo_key_words
        return context