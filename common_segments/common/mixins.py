from tarot_cards.models import TarotSuits


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
