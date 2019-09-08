class ReversedStr(str):
    ## __nwe__ gets used with immutable objects, it does not take self, they operate on class
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self