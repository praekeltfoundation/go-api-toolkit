from zope.interface import Interface


class ICollection(Interface):
    """
    An interface to a collection of objects.
    """

    def all_keys():
        """
        Return an iterable over all keys in the collection. May return a
        deferred instead of the iterable.
        """

    def stream(query):
        """
        Return an iterable over all objects in the collection. The iterable may
        contain deferreds instead of objects. May return a deferred instead of
        the iterable.
        """

    def page(cursor, max_results, query):
        """
        Return (cursor, data), where cursor is a string that refers to the
        next page, and data is an interable over all objects within the page.
        The iterable may contain deferreds instead of objects. May return a
        deffered instead of the iterable
        """

    def get(object_id):
        """
        Return a single object from the collection. May return a deferred
        instead of the object.

        Should raise :class:`CollectionObjectNotFound`` if ``object_id`` refers
        to an object that doesn't exist.
        """

    def create(object_id, data):
        """
        Create an object within the collection and return the new ``object_id``
        and object data. May return a deferred.

        If ``object_id`` is ``None``, an identifier will be generated. Some
        collections may insist on generating their own ``object_id`` and raise
        a :class:`CollectionUsageError` if an ``object_id`` is given.

        Should raise :class:`CollectionObjectAlreadyExists` if ``object_id`` is
        not ``None`` and already exists.
        """

    def update(object_id, data):
        """
        Update an object and return the updated object data. May return a
        deferred.

        ``object_id`` may not be ``None``.

        Should raise :class:`CollectionObjectNotFound`` if ``object_id`` refers
        to an object that doesn't exist.
        """

    def delete(object_id):
        """
        Delete an object and return the deleted object data. May return a
        deferred.

        ``object_id`` may not be ``None``.

        Should raise :class:`CollectionObjectNotFound`` if ``object_id`` refers
        to an object that doesn't exist.
        """
