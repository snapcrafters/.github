# Snapcrafters processes and responsibilities

## Table of Contents

* [Member Types](#member-types)
* [Processes](#processes)
  * [How to become a Snapcrafter](#join-us)
  * [Creating a new snap](#new-snap)
  * [Transfering a snap to upstream](#transfer-to-upstream)
  * [How to contribute to a snap](#contributing)
  * [How to test a snap](#testing)
  * [Adding a new snap to Snapcrafters](#new-snap)

## Member types<a name="member-types"/>

### "Regular" members

* Are "maintainers" of one or more specific snaps. This means they lead the effort to maintain those snaps, although any member can help. The README of a snap should explain who the maintainer is.
* Create and review pull requests to the snaps. To minimize potential mistakes and improve the overall quality of our snaps, we mandate a PR and one review for any change, even if it comes from the maintainer.
* Help build and define the Snapcrafters processes.
* Vet the inclusion of new members.
* Follow the Snapcrafters processes and guidelines.

### Administrators

* Have full access to the GitHub organization and the Snapcrafters publisher in the store.
* Give new members the required privileges.
* Help in transferring snaps to their upstream developers.

## Snapcrafters expectations

* You will have access to the snap repo for a project that is likely not your own. You have a duty of care to ensure that any pushes to stable are tested.
* Before stepping away from Snapcrafters, make your intentions clear so your snaps can be re-homed.

## Processes

### How to become a Snapcrafter<a name="join-us"/>

To become a member of Snapcrafters you must be:

* A member of the [Snapcraft forum](https://forum.snapcraft.io/) for at least six months, and in good standing.
* An active participant in the forum.
* An active maintainer of at least one snap in your own name.

If you fit these criteria then you can follow this process.

1. Create a post on the forum in [the Snapcrafters category](https://forum.snapcraft.io/c/snapcrafters/23) titled `<your-name> | Snapcrafters membership application`, where you give a short intro of your contributions to the snap ecosystem. This includes
   * Which snaps you’ve maintained and for how long.
   * Which other snaps you’ve contributed to.
   * [if applicable] which other snap projects (like `snapcraft`) you’ve contributed to
   * How you want to contribute to snapcrafters.
     * Which existing Snapcrafters snaps do you want to maintain?
     * Or which snaps do you want to bring under the umbrella?
1. We will notify you that we received your application and will discuss it internally. If none of the existing members object and at least one of the Administrators wants to support you, you become a member!
1. After your have been approved, one of the Snapcrafters Admins will be in touch to discuss administrative access.

### Creating a new snap<a name="new-snap"/>

Since our resources are limited, it’s important to see whether it actually makes sense to create a snap for an application.

* Does the application benefit from being in a snap? Snaps are good for fast-moving and hard-to-install applications which are not available in regular distro repositories. Widely available and slow-moving software such as the GNU tools are often not the best candidates to put in a snap.
* Does this application already have a snap? Adopting an existing Snap is always preferred over creating a new one. Try to contact the snap publisher and work with them to either improve their snap or take over maintenance.

If it makes sense to snap the app, start from our [template repository](https://github.com/snapcrafters/fork-and-rename-me) and follow the process described in its README. Update the following settings in the repository you created:

* **Manage Access:** Set up permissions as explained in [Permissions](https://github.com/snapcrafters/.github/wiki/Permissions-and-Secrets)
* **Options:** Disable Wikis, Sponsorships, Projects, and Discussions (unless you’re using one of them).
* **Metadata:**
  * **Description** should be `A community-maintained package to easily install <Snap Name> on Linux`.
  * **Website** should point to the snap in the snap store.

### Transfering a snap to upstream<a name="transfer-to-upstream"/>

Having the upstream developer maintain the snap of their own software is always preferred. If the upstream developer wants to take over maintenance of a snap, follow this process.

1. Verify you are indeed talking to the upstream developer.
1. Ask the developer to create a [Snap Store Brand account](https://snapcraft.io/docs/store-brand-accounts) in the name of the project, if they don’t have one yet.
1. Add the email address of the brand account as a “collaborator” to the snap on https://dashboard.snapcraft.io. A Snapcraft administrator can help with this.
1. Ask the store team [on the forum](https://forum.snapcraft.io) to transfer the snap to the brand account.
1. Ask a Snapcrafter administrator to transfer the snap’s repository or to archive the repository if upstream has their own.

After this process is finished, the snap is not part of Snapcrafters anymore and will not follow these processes anymore. However, even after the transition, we can still assist the developer with any issues they have maintaining the snap.

### Contributing workflow<a name="contributing"/>

For more information on our contribution process, see [our Contributing Guide](https://github.com/snapcrafters/.github/wiki/Contributing).

### Snap testing guidelines<a name="testing"/>

Snapcrafters should follow "good enough" testing. It is more important to test quickly and often than to test thoroughly. We don’t want to slow down our work too much, but we also want to make sure applications still work.

### Adding a new snap to Snapcrafters<a name="new-snap"/>

Any Snapcrafter can add a new snap to our collection, but in general, we should avoid expanding our library until our backlog is addressed. We have a lot of snaps without automation and on very old cores, so we want to fix those before giving ourselves more work.

Take a look at [our dashboard](https://snapcrafters.org/snap-packages/) to see which snaps don't have automation yet. Any snap with CI status "unknown" and with hashes instead of versions is not fully automated yet.

Process:

1. Ask the other Snapcrafters in our Matrix channel whether they think it's a good idea to add a new snap.
2. If nobody objects, ask one of the admins to register the snap name.
3. Fork the template repository, add your snap code and make automation work.
4. Add one of the admins to set up credentials for the automation.
