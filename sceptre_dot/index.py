import sys
from os import getcwd
from os.path import commonprefix

from sceptre.context import SceptreContext
from sceptre.plan.plan import SceptrePlan


def main():
    plan = SceptrePlan(SceptreContext(project_path=getcwd(), command_path=sys.argv[1]))
    plan.resolve(None)

    dependencies = get_dependencies(plan)
    flat_list = [item for sublist in dependencies for item in sublist]
    common_prefix = ''
    if len(flat_list) > 1:
        common_prefix = commonprefix(flat_list)
    print_graph(common_prefix, plan)

    cluster_repr = get_cluster_repr(plan, len(flat_list))
    print(cluster_repr)
    print('  label="Sceptre launch graph{}"'.format(' (prefix: {})'.format(common_prefix) if common_prefix else ''))
    print('  labelloc=top;')
    print('}')


def print_graph(common_prefix, plan):
    print('digraph sceptre {')
    for index, stacks in enumerate(plan.launch_order):
        print('  subgraph cluster{} {{'.format(index))
        for stack in stacks:
            print('    "{}"'.format(stack.name[len(common_prefix):]))
        print('  }\n')


def get_cluster_repr(plan, flat_list_length):
    if flat_list_length < 2:
        return ''
    cluster_repr = '  '
    for index in range(len(plan.launch_order)):
        if index != 0:
            cluster_repr += ' -> '
        cluster_repr += 'cluster{}'.format(index)
    return cluster_repr


def get_dependencies(plan):
    dependencies = []
    for stacks in plan.launch_order:
        group = []
        dependencies.append(group)
        for stack in stacks:
            group.append(stack.name)
    return dependencies


if __name__ == '__main__':
    main()
