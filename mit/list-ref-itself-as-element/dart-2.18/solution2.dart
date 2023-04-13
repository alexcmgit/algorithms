// Dart doesn't support recursive typedefs, like this:
// typedef RecursiveList = List<RecursiveList>; This code throws Typedefs can't reference themselves directly or recursively via another typedef.darttype_alias_cannot_reference_itself
// But we can do it by using classes, though it's not required to examplify this recursive list.

List<dynamic> createRecursiveList() {
  final List<dynamic> l = <dynamic>[null];
  l[0] = l;
  return l;
}
