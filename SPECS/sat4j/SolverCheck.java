import org.sat4j.core.VecInt;
class SolverCheck {
    public static void main(String[] args) throws Exception {
        var sat = org.sat4j.minisat.SolverFactory.newDefault();
        sat.newVar(2);
        sat.addClause(new VecInt(new int[] {1, 2}));
        if (!sat.isSatisfiable() || sat.isSatisfiable(new VecInt(new int[] {-1, -2})))
            throw new AssertionError("CNF assumptions");
        var pb = org.sat4j.pb.SolverFactory.newDefault();
        pb.newVar(2);
        pb.addAtMost(new VecInt(new int[] {1, 2}), 1);
        if (!pb.isSatisfiable(new VecInt(new int[] {1, -2})) || pb.isSatisfiable(new VecInt(new int[] {1, 2})))
            throw new AssertionError("Pseudo-Boolean cardinality");
    }
}
