<p><a href="https://www.beecrowd.com.br/repository/UOJ_2740_en.html">beecrowd.com.br/repository/UOJ_2740_en.html</a></p><hr>
                          <div>
                            <span>URI Online <strong>SQL</strong> | 2740 </span>
                            <h1>League</h1>
                            <div>
                              <p>Marcos Lima <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                            </div>
                            <strong>Timelimit: 1</strong>
                          </div>
                          <div>
                          <div>
                            <p>The International Underground Excavation League is a success between alternative sports, however the staff responsible for organizing the events doesn’t understand computers at all, they only know how to dig and the sport rule set. As such, you were hired to solve the League’s problem. </p>
                            <p>Select the three first placed with the initial phrase "<strong>Podium: </strong>" and select the last two, which will be demoted to a lower league with the initial phrase “<strong>Demoted:</strong>".</p>
                          </div>
                          <div>
                          <h2>Schema</h2>
                          <div>
                          <table>
                          <caption>league</caption>
                          <tbody><tr>
                          <td><strong>Column</strong></td>
                          <td><strong>Type</strong></td>
                        </tr>
                        <tr>
                          <td>position (PK)</td>
                          <td>integer</td>
                        </tr>
                        <tr>
                          <td>team</td>
                          <td>varchar</td>
                        </tr>
                      </tbody></table>
                    </div>
                  </div>
                  <div>
                  <h2>Tables</h2>
                  <div>
                  <table>
                  <caption>league</caption>
                  <tbody><tr>
                  <td><strong>position</strong></td>
                  <td><strong>team</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>The Quack Bats</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>The Responsible Hornets</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>The Bawdy Dolphins</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>The Abstracted Sharks</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>The Nervous Zebras</td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>The Oafish Owls</td>
                </tr>
                <tr>
                  <td>7</td>
                  <td>The Unequaled Bison</td>
                </tr>
                <tr>
                  <td>8</td>
                  <td>The Keen Kangaroos</td>
                </tr>
                <tr>
                  <td>9</td>
                  <td>The Left Nightingales</td>
                </tr>
                <tr>
                  <td>10</td>
                  <td>The Terrific Elks</td>
                </tr>
                <tr>
                  <td>11</td>
                  <td>The Lumpy Frogs</td>
                </tr>
                <tr>
                  <td>12</td>
                  <td>The Swift Buffalo</td>
                </tr>
                <tr>
                  <td>13</td>
                  <td>The Big Chargers</td>
                </tr>
                <tr>
                  <td>14</td>
                  <td>The Rough Robins</td>
                </tr>
                <tr>
                  <td>15</td>
                  <td>The Silver Crocs</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>name</strong></td>
        </tr>
        <tr>
          <td>Podium: The Quack Bats</td>
        </tr>
        <tr>
          <td>Podium: The Responsible Hornets</td>
        </tr>
        <tr>
          <td>Podium: The Bawdy Dolphins</td>
        </tr>
        <tr>
          <td>Demoted: The Rough Robins</td>
        </tr>
        <tr>
          <td>Demoted: The Silver Crocs</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>