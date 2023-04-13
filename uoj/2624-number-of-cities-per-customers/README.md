<p><a href="https://www.beecrowd.com.br/repository/UOJ_2624_en.html">beecrowd.com.br/repository/UOJ_2624_en.html</a></p><hr>
                          <div>
                            <span>URI Online <strong>SQL</strong> | 2624 </span>
                            <h1>Number of Cities per Customers</h1>
                            <div>
                              <p>Paulo R. Rodegheri <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                            </div>
                            <strong>Timelimit: 1</strong>
                          </div>
                          <div>
                          <div>
                            <p>The company board asked you for a simple report on how many cities the company has already reached.</p>
                            <p>To do this you must display the number of distinct cities in the customers table.</p>
                          </div>
                          <div>
                          <h2>Schema</h2>
                          <div>
                          <table>
                          <caption>customers</caption>
                          <tbody><tr>
                          <td><strong>Column</strong></td>
                          <td><strong>Type</strong></td>
                        </tr>
                        <tr>
                          <td>id (PK)</td>
                          <td>numeric</td>
                        </tr>
                        <tr>
                          <td>name</td>
                          <td>character varying (255)</td>
                        </tr>
                        <tr>
                          <td>street</td>
                          <td>character varying (255)</td>
                        </tr>
                        <tr>
                          <td>city</td>
                          <td>character varying (255)</td>
                        </tr>
                        <tr>
                          <td>state</td>
                          <td>char (2)</td>
                        </tr>
                        <tr>
                          <td>credit_limit</td>
                          <td>numeric</td>
                        </tr>
                      </tbody></table>
                    </div>
                  </div>
                  <div>
                  <h2>Tables</h2>
                  <div>
                  <table>
                  <caption>customers</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>name</strong></td>
                  <td><strong>street</strong></td>
                  <td><strong>city</strong></td>
                  <td><strong>state</strong></td>
                  <td><strong>credit_limit</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>Nicolas Diogo Cardoso</td>
                  <td>Acesso Um</td>
                  <td>Porto Alegre</td>
                  <td>RS</td>
                  <td>475</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Cecília Olivia Rodrigues</td>
                  <td>Rua Sizuka Usuy</td>
                  <td>Cianorte</td>
                  <td>PR</td>
                  <td>3170</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Augusto Fernando Carlos Eduardo Cardoso</td>
                  <td>Rua Baldomiro Koerich</td>
                  <td>Palhoça</td>
                  <td>SC</td>
                  <td>1067</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>Nicolas Diogo Cardoso</td>
                  <td>Acesso Um</td>
                  <td>Porto Alegre</td>
                  <td>RS</td>
                  <td>475</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>Sabrina Heloisa Gabriela Barros</td>
                  <td>Rua Engenheiro Tito Marques Fernandes</td>
                  <td>Porto Alegre</td>
                  <td>RS</td>
                  <td>4312</td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>Joaquim Diego Lorenzo Araújo</td>
                  <td>Rua Vitorino</td>
                  <td>Novo Hamburgo</td>
                  <td>RS</td>
                  <td>2314</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>count</strong></td>
        </tr>
        <tr>
          <td>4</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>