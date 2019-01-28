
class CachedChoiceFieldOptionsMixin(object):
    """
    This class speeds up performance of inline foreign-key pickers so we don't have to re-query the options for each item in the list

    From: https://gist.github.com/ninapavlich/e6e90fa25c3882fe83942ddf871302ac
    """

    cached_choice_fields = []

    def formfield_for_dbfield(self, db_field, **kwargs):
        request = kwargs['request']
        formfield = super(CachedChoiceFieldOptionsMixin,
                          self).formfield_for_dbfield(db_field, **kwargs)

        if db_field.name in self.cached_choice_fields:
            cache_key = self.get_cache_key(db_field.name)
            choices = getattr(request, cache_key, None)

            if not choices:
                choices = list(formfield.choices)
                setattr(request, cache_key, choices)

            formfield.choices = choices

        return formfield

    def get_cache_key(self, db_field_name):
        return u'_%s_%s_choices_cache' % (self.model._meta.db_table, db_field_name)
