# Snapcrafters processes and responsibilities

## Table of Contents

* [Member Types](#member-types)
* [Processes](#processes)
  * [How to become a Snapcrafter](#join-us)
  * [Creating a new snap](#new-snap)
  * [Transfering a snap to upstream](#transfer-to-upstream)
  * [How to contribute to a snap](#contributing)
  * [How to test a snap](#testing)

## Member types<a name="member-types"/>

### Core members

* Are "drivers" of one or more specific Snapcrafters snaps. This means they lead the effort to maintain those snaps. They triage issues, fix bugs, and rebuild the snap when there are security updates. See the Snapcrafters snaps tracker for a list of who drives what snap.
* Create and review pull requests to the snaps. To minimize potential mistakes and improve the overall quality of our snaps, we mandate a PR and one review for any change, even if it comes from a "driver".
* Help build and define the Snapcrafters processes.
* Meet on a periodic basis with other Snapcrafters to discuss the processes.
* Vet the inclusion of new members to the pool of core members.
* Responsible for following the Snapcrafters processes and guidelines.
* Participate in the monthly Snapcrafters group meeting * either in person or asynchronously on the forum.
* Participate in the approval of new Snapcrafters. Even if that's just an acknowledgment.

### Administrators

* Administrators are core members who have full access to the GitHub organization and the Snapcrafters publisher in the store.
* Give new core members the required privileges.
* Help in transferring snaps to their upstream developers.

### Regular members

* Contribute pull requests.
* Report issues and bugs.
* Run tests for new builds or revisions.
* Help automate processes.

Anyone can be a regular member and contribute to our snaps in this way. We only make the distinction so you, the contributor, can see some of the things you could do to help.

## Snapcrafters expectations

* You will have access to the snap repo for a project that is likely not your own. You have a duty of care to ensure that any pushes to stable are tested.
* The Snapcrafters quorum during the monthly meeting can arrange to change the process, elect new Snapcrafters, or remove Snapcrafters.
* Before stepping away from Snapcrafters, make your intentions clear so your snaps can be re-homed.

## Processes

### How to become a Snapcrafter<a name="join-us"/>

To become a core member of Snapcrafters you must be:

* A member of the [Snapcraft forum](https://forum.snapcraft.io/) for at least six months, and in good standing.
* An active participant in the forum.
* An active maintainer of at least one snap in your own name.
* Sponsored by an admin or an existing Snapcrafters core member.

If you fit these criteria or have a strong argument why you should be considered anyway then add a comment on the Snapcrafters reboot post](https://forum.snapcraft.io/t/snapcrafters-reboot/24625) to tell us, and the rest of the community, about your snaps. Also tell us the Snapcrafters snaps that you would like to take on. Ideally you have familiarity with the snaps you request. State the different ways of contribution and participation you’d like to be involved in. After your have been approved, we will be in touch to discuss administrative access and co-ordinate your first Snapcrafters meeting.

### Creating a new snap<a name="new-snap"/>

Since our resources are limited, it’s important to see whether it actually makes sense to create a snap for an application.

* Does the application benefit from being in a snap? Snaps are good for fast-moving and hard-to-install applications which are not available in regular distro repositories. Widely available and slow-moving software such as the GNU tools are often not the best candidates to put in a snap.
* Does this application already have a snap? Adopting an existing Snap is always preferred over creating a new one. Try to contact the snap publisher and work with them to either improve their snap or take over maintenance.

If it makes sense to snap the app, start from our [template repository](https://github.com/snapcrafters/fork-and-rename-me) and follow the process described in its README. Update the following settings in the repository you created:

* **Manage Access:** Give the `@reviewers` team `maintain` access to the repository.
* **Branches:** Create a branch protection rule with the pattern `*` which requires 1 approving review before merging. Check "include administrators".
* **Options:** Disable Wikis, Sponsorships, Projects, and Discussions (unless you’re using one of them).

### Transfering a snap to upstream<a name="transfer-to-upstream"/>

Having the upstream developer maintain the snap of their own software is always preferred. If the upstream developer wants to take over maintenance of a snap, follow this process.

1. Verify you are indeed talking to the upstream developer.
1. Ask the developer to create a [Snap Store Brand account](https://snapcraft.io/docs/store-brand-accounts) in the name of the project, if they don’t have one yet.
1. Add the email address of the brand account as a “collaborator” to the snap on https://dashboard.snapcraft.io. A Snapcraft administrator can help with this.
1. Ask the store team [on the forum](https://forum.snapcraft.io) to transfer the snap to the brand account.
1. Ask a Snapcrafter administrator to transfer the snap’s repository or to archive the repository if upstream has their own.

After this process is finished, the snap is not part of Snapcrafters anymore and will not follow these processes anymore. However, even after the transition, we can still assist the developer with any issues they have maintaining the snap.

### Contributing workflow<a name="contributing"/>

Both external contributors _and maintainers_ use this workflow to update the snap.

1. Create a personal fork of the repository.
1. Update the code and push to your personal fork.
1. Create a PR and ask for a review from `@reviewers`. Feel free to ping people personally too. You need at least one positive review from a core member.
1. When the code is merged, the automatic build will push a release to the `edge` channel.
1. Create a “call for testing” on the forum and ask people to test the `edge` channel.
1. If those tests are successful, publish the release to the `stable` channel.

### Snap testing guidelines<a name="testing"/>

Testing is the next step beyond rebooting snapcrafters. Putting in place a structured process to build, test, and automate the maintenance of snaps. In the beginning snapcrafters should follow the guide to ‘good enough’ testing. In the future Igor will lead the collaboration with the Desktop and Certifications teams to properly formalise a process that snapcrafters can easily use.

#### Good enough’ snap testing

It is more important to test quickly and often than to test thoroughly. We don’t want to slow down our work too much, but we also want to make sure applications still work.
