# AWSCustom::EBSCustom::EBSSnapshotCustom

Custom resource to store in AWS Config EBS Snapshot information

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "AWSCustom::EBSCustom::EBSSnapshotCustom",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ownerid" title="OwnerId">OwnerId</a>" : <i>String</i>,
        "<a href="#encrypted" title="Encrypted">Encrypted</a>" : <i>Boolean</i>,
        "<a href="#progress" title="Progress">Progress</a>" : <i>String</i>,
        "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#volumeid" title="VolumeId">VolumeId</a>" : <i>String</i>,
        "<a href="#volumesize" title="VolumeSize">VolumeSize</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: AWSCustom::EBSCustom::EBSSnapshotCustom
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ownerid" title="OwnerId">OwnerId</a>: <i>String</i>
    <a href="#encrypted" title="Encrypted">Encrypted</a>: <i>Boolean</i>
    <a href="#progress" title="Progress">Progress</a>: <i>String</i>
    <a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#volumeid" title="VolumeId">VolumeId</a>: <i>String</i>
    <a href="#volumesize" title="VolumeSize">VolumeSize</a>: <i>String</i>
</pre>

## Properties

#### Description

Description of the snapshot

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerId

Account ID of the owner of the snapshot

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encrypted

Weather the snapshot is encrypted or not

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Progress

Progress of the snapshot

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

ID of The Snapshot

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

State of the snapshot

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeId

ID of The Volume

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeSize

ID of The Volume

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the SnapshotId.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### SnapshotId

ID of The Snapshot

