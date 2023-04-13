extension PowerSet<T> on Iterable<T> {
  Iterable<Iterable<T>> _computePowerset({
    required int index,
    required Iterable<T> sourceSet,
    required Iterable<T> powerSet,
  }) {
    if (index == length) {
      return <Iterable<T>>[powerSet];
    }

    return <Iterable<T>>[
      ..._computePowerset(
        index: index + 1,
        sourceSet: sourceSet,
        powerSet: <T>[...powerSet, sourceSet.elementAt(index)],
      ),
      ..._computePowerset(
        index: index + 1,
        sourceSet: sourceSet,
        powerSet: <T>[...powerSet],
      ),
    ];
  }

  Iterable<Iterable<T>> powerset() {
    return _computePowerset(
      index: 0,
      sourceSet: this,
      powerSet: <T>[],
    );
  }
}

List<List<int>> powerset(List<int> source) =>
    source.powerset().map((Iterable<int> e) => e.toList()).toList();
