import pytest
from nemli.commands.utility.summarize import response_to_list

test_inputs = dict(
    single_small=dict(
        header="",
        msg_char_lim=200,
        raw=(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque gravida id dui sit amet posuere."
            " Proin et purus vitae ipsum malesuada consequat quis vel nulla. Vestibulum ante ipsum primis in."
        ),
        expected=[
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque gravida id dui sit amet posuere."
            " Proin et purus vitae ipsum malesuada consequat quis vel nulla. Vestibulum ante ipsum primis in."
        ],
    ),
    single_big=dict(
        header="",
        msg_char_lim=300,
        raw=(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam mattis turpis sem, non volutpat ligula"
            " porttitor id. Pellentesque dignissim mattis molestie. In vel leo elementum, lobortis ligula quis, blandit"
            " felis. Proin id ornare nulla. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc at"
            " tempor arcu, eget interdum elit. Quisque pellentesque mollis augue vitae faucibus. Curabitur sagittis"
            " elit facilisis justo vestibulum, ut ullamcorper lacus eleifend. Integer eu efficitur velit, quis vehicula"
            " tortor. Praesent dignissim vulputate ante sit amet rhoncus. Ut dolor ligula, varius tempor est et,"
            " lobortis aliquet ligula. Donec vitae pharetra urna, sed porttitor urna. Pellentesque sit amet commodo mi,"
            " ut euismod neque. Cras egestas non metus ac luctus. Fusce pellentesque imperdiet purus eu scelerisque."
            " Suspendisse condimentum sem dui, eu efficitur felis tristique nec."
        ),
        expected=[
            (
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam mattis turpis sem, non volutpat ligula"
                " porttitor id. Pellentesque dignissim mattis molestie. In vel leo elementum, lobortis ligula quis,"
                " blandit felis. Proin id ornare nulla. Interdum et malesuada fames ac ante ipsum primis in"
                " faucibus. Nu"
            ),
            (
                "nc at tempor arcu, eget interdum elit. Quisque pellentesque mollis augue vitae faucibus. Curabitur"
                " sagittis elit facilisis justo vestibulum, ut ullamcorper lacus eleifend. Integer eu efficitur velit,"
                " quis vehicula tortor. Praesent dignissim vulputate ante sit amet rhoncus. Ut dolor ligula, varius te"
            ),
            (
                "mpor est et, lobortis aliquet ligula. Donec vitae pharetra urna, sed porttitor urna. Pellentesque sit"
                " amet commodo mi, ut euismod neque. Cras egestas non metus ac luctus. Fusce pellentesque imperdiet"
                " purus eu scelerisque. Suspendisse condimentum sem dui, eu efficitur felis tristique nec."
            ),
        ],
    ),
    lines=dict(
        header="",
        msg_char_lim=1500,
        raw="""\
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean
venenatis nunc vel ipsum tempor iaculis. Mauris fringilla consequat
erat ut molestie. Etiam ex orci, rutrum vitae nibh eget, maximus
rutrum libero. Etiam interdum consectetur lobortis. Aenean porta velit
ac nisi iaculis venenatis vel eget nunc. Vestibulum euismod convallis
lorem, sed malesuada felis. Sed mollis vehicula massa, a dignissim
diam. Maecenas molestie tristique finibus.

Duis mauris metus, interdum at porta vel, rhoncus sit amet
massa. Phasellus malesuada vestibulum arcu, eu interdum
libero. Aliquam interdum libero a posuere cursus. Aenean in commodo
est. Sed vitae leo vitae justo imperdiet vehicula volutpat at
mauris. Nunc id mauris eu augue volutpat porta in sit amet
mauris. Nulla ex odio, scelerisque at nisi at, semper suscipit
nisl. Aliquam consectetur velit libero, a auctor ligula lobortis
eu. Sed posuere neque sed nibh viverra, et dictum dolor
condimentum. Curabitur commodo nunc nisl, at vestibulum tortor
tincidunt quis. Phasellus tincidunt erat ac justo congue, at dictum
justo congue. Pellentesque sollicitudin justo quis felis luctus, ut
consequat nibh luctus.

Nunc gravida sem turpis, vitae laoreet eros feugiat ut. Vestibulum
pharetra, orci in rhoncus venenatis, nibh elit viverra arcu, a
vehicula urna magna at dui. Etiam euismod dapibus luctus. Curabitur
dapibus accumsan lorem ornare ultrices. Proin nunc arcu, convallis in
orci suscipit, pharetra varius lacus. Nullam imperdiet orci ac metus
laoreet, in elementum magna tincidunt. Pellentesque tortor lorem,
placerat sed commodo in, imperdiet sed risus. Pellentesque sagittis
tellus sodales auctor mattis. Fusce interdum urna ut sapien luctus
porttitor. In tincidunt molestie scelerisque. Suspendisse id sem et
risus pulvinar volutpat nec id leo.

Quisque vitae risus pretium, mollis ipsum ac, ultrices nibh. Cras
pellentesque maximus fringilla. Vivamus vitae tempor odio. Cras ac
pellentesque dui. Vestibulum volutpat bibendum nunc, nec consectetur
massa porta et. Duis ultrices mauris at eros mattis hendrerit. Nullam
quis imperdiet est. Sed non gravida quam. Phasellus at elit accumsan,
suscipit tellus vitae, pharetra felis. Donec vulputate erat quis
posuere tempor.

Etiam congue mauris in neque cursus, in cursus purus viverra. Quisque
sit amet ligula eu massa laoreet maximus a ut tellus. Sed in magna
nunc. Vestibulum id elit sed ex sagittis rhoncus a vel est. Fusce
rutrum dapibus metus, vel eleifend leo placerat vel. Donec condimentum
velit massa, quis hendrerit neque maximus eu. Proin ac felis vel leo
faucibus blandit. Etiam risus metus, lacinia eu ultrices id, aliquam
facilisis risus. Nam at semper nibh, quis commodo arcu. In hac
habitasse platea dictumst. Phasellus sed rutrum lacus, et cursus
tortor. Etiam imperdiet elit egestas maximus placerat. Maecenas
convallis accumsan viverra. Praesent enim nibh, dignissim ac mollis
quis, scelerisque eu nibh. Vestibulum a turpis id est ullamcorper
viverra. Sed non aliquet lacus, non volutpat dolor.
""",
        expected=[
            """\
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean
venenatis nunc vel ipsum tempor iaculis. Mauris fringilla consequat
erat ut molestie. Etiam ex orci, rutrum vitae nibh eget, maximus
rutrum libero. Etiam interdum consectetur lobortis. Aenean porta velit
ac nisi iaculis venenatis vel eget nunc. Vestibulum euismod convallis
lorem, sed malesuada felis. Sed mollis vehicula massa, a dignissim
diam. Maecenas molestie tristique finibus.

Duis mauris metus, interdum at porta vel, rhoncus sit amet
massa. Phasellus malesuada vestibulum arcu, eu interdum
libero. Aliquam interdum libero a posuere cursus. Aenean in commodo
est. Sed vitae leo vitae justo imperdiet vehicula volutpat at
mauris. Nunc id mauris eu augue volutpat porta in sit amet
mauris. Nulla ex odio, scelerisque at nisi at, semper suscipit
nisl. Aliquam consectetur velit libero, a auctor ligula lobortis
eu. Sed posuere neque sed nibh viverra, et dictum dolor
condimentum. Curabitur commodo nunc nisl, at vestibulum tortor
tincidunt quis. Phasellus tincidunt erat ac justo congue, at dictum
justo congue. Pellentesque sollicitudin justo quis felis luctus, ut
consequat nibh luctus.

Nunc gravida sem turpis, vitae laoreet eros feugiat ut. Vestibulum
pharetra, orci in rhoncus venenatis, nibh elit viverra arcu, a
vehicula urna magna at dui. Etiam euismod dapibus luctus. Curabitur
dapibus accumsan lorem ornare ultrices. Proin nunc arcu, convallis in
orci suscipit, pharetra varius lacus. Nullam imperdiet orci ac metus""",
            """
laoreet, in elementum magna tincidunt. Pellentesque tortor lorem,
placerat sed commodo in, imperdiet sed risus. Pellentesque sagittis
tellus sodales auctor mattis. Fusce interdum urna ut sapien luctus
porttitor. In tincidunt molestie scelerisque. Suspendisse id sem et
risus pulvinar volutpat nec id leo.

Quisque vitae risus pretium, mollis ipsum ac, ultrices nibh. Cras
pellentesque maximus fringilla. Vivamus vitae tempor odio. Cras ac
pellentesque dui. Vestibulum volutpat bibendum nunc, nec consectetur
massa porta et. Duis ultrices mauris at eros mattis hendrerit. Nullam
quis imperdiet est. Sed non gravida quam. Phasellus at elit accumsan,
suscipit tellus vitae, pharetra felis. Donec vulputate erat quis
posuere tempor.

Etiam congue mauris in neque cursus, in cursus purus viverra. Quisque
sit amet ligula eu massa laoreet maximus a ut tellus. Sed in magna
nunc. Vestibulum id elit sed ex sagittis rhoncus a vel est. Fusce
rutrum dapibus metus, vel eleifend leo placerat vel. Donec condimentum
velit massa, quis hendrerit neque maximus eu. Proin ac felis vel leo
faucibus blandit. Etiam risus metus, lacinia eu ultrices id, aliquam
facilisis risus. Nam at semper nibh, quis commodo arcu. In hac
habitasse platea dictumst. Phasellus sed rutrum lacus, et cursus
tortor. Etiam imperdiet elit egestas maximus placerat. Maecenas
convallis accumsan viverra. Praesent enim nibh, dignissim ac mollis
quis, scelerisque eu nibh. Vestibulum a turpis id est ullamcorper""",
            """
viverra. Sed non aliquet lacus, non volutpat dolor.
""",
        ],
    ),
    topics=dict(
        header="",
        msg_char_lim=2000,
        raw="""\
# Header 1
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean
venenatis nunc vel ipsum tempor iaculis. Mauris fringilla consequat
erat ut molestie. Etiam ex orci, rutrum vitae nibh eget, maximus
rutrum libero. Etiam interdum consectetur lobortis. Aenean porta velit
ac nisi iaculis venenatis vel eget nunc. Vestibulum euismod convallis
lorem, sed malesuada felis. Sed mollis vehicula massa, a dignissim
diam. Maecenas molestie tristique finibus.

Duis mauris metus, interdum at porta vel, rhoncus sit amet
massa. Phasellus malesuada vestibulum arcu, eu interdum
libero. Aliquam interdum libero a posuere cursus. Aenean in commodo
est. Sed vitae leo vitae justo imperdiet vehicula volutpat at
mauris. Nunc id mauris eu augue volutpat porta in sit amet
mauris. Nulla ex odio, scelerisque at nisi at, semper suscipit
nisl. Aliquam consectetur velit libero, a auctor ligula lobortis
eu. Sed posuere neque sed nibh viverra, et dictum dolor
condimentum. Curabitur commodo nunc nisl, at vestibulum tortor
tincidunt quis. Phasellus tincidunt erat ac justo congue, at dictum
justo congue. Pellentesque sollicitudin justo quis felis luctus, ut
consequat nibh luctus.

## Header 1.2

Nunc gravida sem turpis, vitae laoreet eros feugiat ut. Vestibulum
pharetra, orci in rhoncus venenatis, nibh elit viverra arcu, a
vehicula urna magna at dui. Etiam euismod dapibus luctus. Curabitur
dapibus accumsan lorem ornare ultrices. Proin nunc arcu, convallis in
orci suscipit, pharetra varius lacus. Nullam imperdiet orci ac metus
laoreet, in elementum magna tincidunt. Pellentesque tortor lorem,
placerat sed commodo in, imperdiet sed risus. Pellentesque sagittis
tellus sodales auctor mattis. Fusce interdum urna ut sapien luctus
porttitor. In tincidunt molestie scelerisque. Suspendisse id sem et
risus pulvinar volutpat nec id leo.

Quisque vitae risus pretium, mollis ipsum ac, ultrices nibh. Cras
pellentesque maximus fringilla. Vivamus vitae tempor odio. Cras ac
pellentesque dui. Vestibulum volutpat bibendum nunc, nec consectetur
massa porta et. Duis ultrices mauris at eros mattis hendrerit. Nullam
quis imperdiet est. Sed non gravida quam. Phasellus at elit accumsan,
suscipit tellus vitae, pharetra felis. Donec vulputate erat quis
posuere tempor.

# Header 2

Etiam congue mauris in neque cursus, in cursus purus viverra. Quisque
sit amet ligula eu massa laoreet maximus a ut tellus. Sed in magna
nunc. Vestibulum id elit sed ex sagittis rhoncus a vel est. Fusce
rutrum dapibus metus, vel eleifend leo placerat vel. Donec condimentum
velit massa, quis hendrerit neque maximus eu. Proin ac felis vel leo
faucibus blandit. Etiam risus metus, lacinia eu ultrices id, aliquam
facilisis risus. Nam at semper nibh, quis commodo arcu. In hac
habitasse platea dictumst. Phasellus sed rutrum lacus, et cursus
tortor. Etiam imperdiet elit egestas maximus placerat. Maecenas
convallis accumsan viverra. Praesent enim nibh, dignissim ac mollis
quis, scelerisque eu nibh. Vestibulum a turpis id est ullamcorper
viverra. Sed non aliquet lacus, non volutpat dolor.

## Header 2.1

Ut ornare egestas purus, non bibendum arcu aliquam eu. Phasellus
luctus lectus eget dolor aliquam pulvinar. Pellentesque vel sagittis
arcu, ut faucibus turpis. Mauris pretium sollicitudin purus ac
iaculis. Duis nec massa sapien. Aenean augue ex, hendrerit sit amet
dignissim quis, cursus ut dui. Fusce suscipit, ipsum eu venenatis
condimentum, enim arcu tempor mauris, id bibendum urna elit id diam.

## Header 2.2

Nulla mattis dolor gravida, aliquet risus sed, scelerisque ante. Donec
eleifend, diam vitae auctor fringilla, urna massa consectetur ipsum,
eget interdum mauris neque sit amet lorem. Sed laoreet egestas
interdum. Cras iaculis malesuada justo, quis dapibus leo. Donec
venenatis magna quam, sit amet molestie est lobortis at. Aliquam
mollis mauris felis. Donec ut risus eu erat euismod vestibulum vitae
volutpat nibh. Quisque sollicitudin arcu at velit feugiat
consectetur. In in convallis enim. Cras condimentum vehicula ante id
lacinia. Suspendisse tempus pulvinar turpis vel aliquet. Sed imperdiet
leo vel dolor tristique, non sagittis nulla commodo.

### Header 2.2.1

Quisque accumsan rhoncus venenatis. Mauris tempor tempus
ultrices. Nullam varius elit et venenatis sollicitudin. Aliquam eget
elementum justo. Pellentesque enim erat, aliquam vel massa vel,
tristique sodales tortor. Aliquam at mi nisi. Maecenas laoreet
eleifend arcu, vitae luctus metus sagittis in.

### Header 2.2.2

Aenean vel leo vitae sapien fermentum tristique. Nullam a odio rutrum
orci aliquet rhoncus vitae nec massa. Phasellus porta elit non odio
imperdiet, eget lacinia mauris suscipit. Morbi vestibulum tempus
fringilla. Orci varius natoque penatibus et magnis dis parturient
montes, nascetur ridiculus mus. Nullam laoreet, leo non luctus tempus,
mi felis venenatis risus, vitae bibendum dui augue vitae augue. Proin
placerat, est et elementum finibus, neque massa tristique urna, id
consectetur orci dui eget risus. Etiam cursus erat vehicula, porttitor
nisl ac, convallis elit.

In faucibus ligula diam, vitae malesuada augue maximus in. Vestibulum
ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia
curae; Fusce nec maximus neque. Duis pellentesque metus in justo
eleifend lobortis. Nunc hendrerit, tortor ut porttitor ultricies,
justo justo imperdiet augue, nec venenatis leo lacus ut sem. Donec
nibh risus, consectetur ut ultrices id, tincidunt rutrum leo. Aenean
maximus tellus malesuada massa maximus, quis tempor urna congue. In
convallis ipsum a odio hendrerit, in venenatis nunc posuere. Donec
vestibulum mi quam. Nam leo risus, iaculis non sem et, tempus eleifend
libero. Etiam fringilla efficitur est, in mollis arcu elementum
ac. Curabitur accumsan sodales orci, non consequat leo dapibus
eget. Vivamus lacinia velit eget velit consectetur hendrerit. Duis at
risus leo. Nullam sapien lacus, molestie vitae nulla vitae, lacinia
vulputate erat. Sed sapien risus, mollis et odio at, mollis laoreet
mi.
""",
        expected=[
            """\
# Header 1
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean
venenatis nunc vel ipsum tempor iaculis. Mauris fringilla consequat
erat ut molestie. Etiam ex orci, rutrum vitae nibh eget, maximus
rutrum libero. Etiam interdum consectetur lobortis. Aenean porta velit
ac nisi iaculis venenatis vel eget nunc. Vestibulum euismod convallis
lorem, sed malesuada felis. Sed mollis vehicula massa, a dignissim
diam. Maecenas molestie tristique finibus.

Duis mauris metus, interdum at porta vel, rhoncus sit amet
massa. Phasellus malesuada vestibulum arcu, eu interdum
libero. Aliquam interdum libero a posuere cursus. Aenean in commodo
est. Sed vitae leo vitae justo imperdiet vehicula volutpat at
mauris. Nunc id mauris eu augue volutpat porta in sit amet
mauris. Nulla ex odio, scelerisque at nisi at, semper suscipit
nisl. Aliquam consectetur velit libero, a auctor ligula lobortis
eu. Sed posuere neque sed nibh viverra, et dictum dolor
condimentum. Curabitur commodo nunc nisl, at vestibulum tortor
tincidunt quis. Phasellus tincidunt erat ac justo congue, at dictum
justo congue. Pellentesque sollicitudin justo quis felis luctus, ut
consequat nibh luctus.
""",
            """\

## Header 1.2

Nunc gravida sem turpis, vitae laoreet eros feugiat ut. Vestibulum
pharetra, orci in rhoncus venenatis, nibh elit viverra arcu, a
vehicula urna magna at dui. Etiam euismod dapibus luctus. Curabitur
dapibus accumsan lorem ornare ultrices. Proin nunc arcu, convallis in
orci suscipit, pharetra varius lacus. Nullam imperdiet orci ac metus
laoreet, in elementum magna tincidunt. Pellentesque tortor lorem,
placerat sed commodo in, imperdiet sed risus. Pellentesque sagittis
tellus sodales auctor mattis. Fusce interdum urna ut sapien luctus
porttitor. In tincidunt molestie scelerisque. Suspendisse id sem et
risus pulvinar volutpat nec id leo.

Quisque vitae risus pretium, mollis ipsum ac, ultrices nibh. Cras
pellentesque maximus fringilla. Vivamus vitae tempor odio. Cras ac
pellentesque dui. Vestibulum volutpat bibendum nunc, nec consectetur
massa porta et. Duis ultrices mauris at eros mattis hendrerit. Nullam
quis imperdiet est. Sed non gravida quam. Phasellus at elit accumsan,
suscipit tellus vitae, pharetra felis. Donec vulputate erat quis
posuere tempor.

# Header 2

Etiam congue mauris in neque cursus, in cursus purus viverra. Quisque
sit amet ligula eu massa laoreet maximus a ut tellus. Sed in magna
nunc. Vestibulum id elit sed ex sagittis rhoncus a vel est. Fusce
rutrum dapibus metus, vel eleifend leo placerat vel. Donec condimentum
velit massa, quis hendrerit neque maximus eu. Proin ac felis vel leo
faucibus blandit. Etiam risus metus, lacinia eu ultrices id, aliquam
facilisis risus. Nam at semper nibh, quis commodo arcu. In hac
habitasse platea dictumst. Phasellus sed rutrum lacus, et cursus
tortor. Etiam imperdiet elit egestas maximus placerat. Maecenas
convallis accumsan viverra. Praesent enim nibh, dignissim ac mollis
quis, scelerisque eu nibh. Vestibulum a turpis id est ullamcorper
viverra. Sed non aliquet lacus, non volutpat dolor.
""",
            """\

## Header 2.1

Ut ornare egestas purus, non bibendum arcu aliquam eu. Phasellus
luctus lectus eget dolor aliquam pulvinar. Pellentesque vel sagittis
arcu, ut faucibus turpis. Mauris pretium sollicitudin purus ac
iaculis. Duis nec massa sapien. Aenean augue ex, hendrerit sit amet
dignissim quis, cursus ut dui. Fusce suscipit, ipsum eu venenatis
condimentum, enim arcu tempor mauris, id bibendum urna elit id diam.

## Header 2.2

Nulla mattis dolor gravida, aliquet risus sed, scelerisque ante. Donec
eleifend, diam vitae auctor fringilla, urna massa consectetur ipsum,
eget interdum mauris neque sit amet lorem. Sed laoreet egestas
interdum. Cras iaculis malesuada justo, quis dapibus leo. Donec
venenatis magna quam, sit amet molestie est lobortis at. Aliquam
mollis mauris felis. Donec ut risus eu erat euismod vestibulum vitae
volutpat nibh. Quisque sollicitudin arcu at velit feugiat
consectetur. In in convallis enim. Cras condimentum vehicula ante id
lacinia. Suspendisse tempus pulvinar turpis vel aliquet. Sed imperdiet
leo vel dolor tristique, non sagittis nulla commodo.

### Header 2.2.1

Quisque accumsan rhoncus venenatis. Mauris tempor tempus
ultrices. Nullam varius elit et venenatis sollicitudin. Aliquam eget
elementum justo. Pellentesque enim erat, aliquam vel massa vel,
tristique sodales tortor. Aliquam at mi nisi. Maecenas laoreet
eleifend arcu, vitae luctus metus sagittis in.
""",
            """\

### Header 2.2.2

Aenean vel leo vitae sapien fermentum tristique. Nullam a odio rutrum
orci aliquet rhoncus vitae nec massa. Phasellus porta elit non odio
imperdiet, eget lacinia mauris suscipit. Morbi vestibulum tempus
fringilla. Orci varius natoque penatibus et magnis dis parturient
montes, nascetur ridiculus mus. Nullam laoreet, leo non luctus tempus,
mi felis venenatis risus, vitae bibendum dui augue vitae augue. Proin
placerat, est et elementum finibus, neque massa tristique urna, id
consectetur orci dui eget risus. Etiam cursus erat vehicula, porttitor
nisl ac, convallis elit.

In faucibus ligula diam, vitae malesuada augue maximus in. Vestibulum
ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia
curae; Fusce nec maximus neque. Duis pellentesque metus in justo
eleifend lobortis. Nunc hendrerit, tortor ut porttitor ultricies,
justo justo imperdiet augue, nec venenatis leo lacus ut sem. Donec
nibh risus, consectetur ut ultrices id, tincidunt rutrum leo. Aenean
maximus tellus malesuada massa maximus, quis tempor urna congue. In
convallis ipsum a odio hendrerit, in venenatis nunc posuere. Donec
vestibulum mi quam. Nam leo risus, iaculis non sem et, tempus eleifend
libero. Etiam fringilla efficitur est, in mollis arcu elementum
ac. Curabitur accumsan sodales orci, non consequat leo dapibus
eget. Vivamus lacinia velit eget velit consectetur hendrerit. Duis at
risus leo. Nullam sapien lacus, molestie vitae nulla vitae, lacinia
vulputate erat. Sed sapien risus, mollis et odio at, mollis laoreet
mi.
""",
        ],
    ),
)


@pytest.fixture(params=test_inputs.values(), ids=list(test_inputs.keys()))
def input_data(request):
    return (
        request.param["header"],
        request.param["msg_char_lim"],
        request.param["raw"],
        request.param["expected"],
    )


def test_response_to_list(input_data):
    header, msg_char_lim, raw, expected = input_data
    for i, resp in enumerate(response_to_list(raw, header, msg_char_lim=msg_char_lim)):
        assert resp == expected[i]
